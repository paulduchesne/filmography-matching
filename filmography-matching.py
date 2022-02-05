#!/usr/bin/env python3
# coding: utf-8

# load libraries.

import numpy
import pandas
import pathlib
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
        self.creator_name = df.to_dict('records')[0]['creator_name']
        self.creator_id = i
        self.filmography = pydash.uniq([x['work_name'] for x in df.to_dict('records')])
        self.accepted = list()

    def identify_candidates(self, r):

        # derive a list of possible matches based on creator name similarity.

        wikidata_creator_names = [str(x) for x in r.creator_name.unique()]
        candidates = process.extract(str(self.creator_name), wikidata_creator_names, limit=1000, scorer=fuzz.token_sort_ratio)
        limited = r.copy()
        limited = limited.loc[limited.creator_name.isin([x[0] for x in candidates if x[1] > 70])]
        self.candidates = list(limited.creator_id.unique())

    def score_candidate(self, n, r):

        # assess individual candidate by pulling median filmographic title match.

        scores = list()

        candidate_titles = r.copy()
        candidate_titles = candidate_titles.loc[candidate_titles.creator_id.isin([n])]

        for f in self.filmography:
            match = process.extractOne(f, list(candidate_titles.work_name.unique()), scorer=fuzz.token_sort_ratio)
            scores.append(match[1])

        if numpy.median(scores) == 100:
            self.accepted.append(n)

def filmography_matching(d1, d2, output):

    # function to process matching creator by creator.

    results = pandas.DataFrame(columns=[d1.name, d2.name])

    d1_df, d2_df = pandas.read_csv(d1), pandas.read_csv(d2)

    d1_creator_id = list(d1_df.creator_id.unique())

    for c in tqdm.tqdm(d1_creator_id):

        m = matchmaker(c, d1_df)
        m.identify_candidates(d2_df)

        for y in m.candidates:
            m.score_candidate(y, d2_df)

        if len(m.accepted) == 1:
            results.loc[len(results)] = [(c), (m.accepted[0])]

    results.to_csv(output, index=False)

if __name__ == "__main__":

    # define inputs and outputs. 

    a = pathlib.Path.cwd() / 'data' / 'data-1.csv'
    b = pathlib.Path.cwd() / 'data' / 'data-2.csv'
    output = pathlib.Path.cwd() / 'results' / 'results.csv'

    filmography_matching(a, b, output)