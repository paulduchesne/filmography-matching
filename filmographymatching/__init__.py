#!/usr/bin/env python3
# coding: utf-8

# load libraries.

import numpy
import pandas
import pydash
import tqdm
from thefuzz import process
from thefuzz import fuzz

# define matching class.

class matchmaker:

    def __init__(self, i, l):

        # instantiate matching instance with intial creator data.

        df = l.copy()
        df = df.loc[df.creator_id.isin([i])]
        self.creator = pydash.uniq([(x['creator_name'], x['creator_id']) for x in df.to_dict('records')])[0]
        self.filmography = pydash.uniq([(x['work_name'], x['work_id']) for x in df.to_dict('records')])
        self.accepted = list()

    def identify_candidates(self, r):

        # derive a list of possible matches based on creator name similarity.

        wikidata_creator_names = [str(x) for x in r.creator_name.unique()]
        candidates = process.extract(str(self.creator[0]), wikidata_creator_names, limit=1000, scorer=fuzz.token_sort_ratio)
        limited = r.copy()
        limited = limited.loc[limited.creator_name.isin([x[0] for x in candidates if x[1] > 70])]
        self.candidates = list(limited.creator_id.unique())

    def score_candidate(self, n, r):

        # assess individual candidate by pulling median filmographic title match.

        scores = list()
        self.title_match = list()

        candidate_titles = r.copy()
        candidate_titles = candidate_titles.loc[candidate_titles.creator_id.isin([n])]
        candidate_titles = pydash.uniq([(x['work_name'], x['work_id']) for x in candidate_titles.to_dict('records')])

        for f in self.filmography:
            match = process.extractOne(f[0], list([x[0] for x in candidate_titles]), scorer=fuzz.token_sort_ratio)
            scores.append(match[1])

            if match[1] >= 100: # set to 100, but could likely go lower.
                t = [x[1] for x in candidate_titles if x[0] == match[0]]
                if len(t) == 1:
                    self.title_match.append((f[1], t[0]))

        if numpy.median(scores) == 100:
            self.accepted.append((n, self.title_match)) 

def match(d1, d2, output):

    # function to process matching creator by creator.

    results = pandas.DataFrame(columns=[f'{d1.stem}-creator', f'{d2.stem}-creator', f'{d1.stem}-work', f'{d2.stem}-work'])
    d1_df, d2_df = pandas.read_csv(d1), pandas.read_csv(d2)
    d1_creator_id = list(d1_df.creator_id.unique())

    for c in tqdm.tqdm(d1_creator_id):

        m = matchmaker(c, d1_df)
        m.identify_candidates(d2_df)

        for y in m.candidates:
            m.score_candidate(y, d2_df)

        if len(m.accepted) == 1:
            for w in m.accepted[0][1]: # in theory we could have a matching creator with no title match.
                results.loc[len(results)] = [(c), (m.accepted[0][0]), (w[0]), (w[1])]

    results.to_csv(output, index=False)