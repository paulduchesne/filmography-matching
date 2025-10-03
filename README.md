# Filmography Matching

Creator matching between filmographic datasets. 

**Introduction**

This work is based on suggestions by Georg Eckes, around filmography matching being significantly more reliable when considering not just individual name and film title similarity, but title similarity over multiple filmography entries between creators. The provided notebook automates this concept between two agent/title datasets.

**Datasets**

Two test datasets are provided, of Australian films from [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) (data1.csv), and Australian films from the [ACMI API](https://github.com/ACMILabs/acmi-api/tree/main) (data2.csv). Both data sources are released as CC0, permitting their inclusion here.

**Method**

For each agent, the script assembles an initial list of match candidates based on name (Levenshtein distance) similarity. Each candidate is assessed by attempting to find the best match from their filmographies with each film of the original agent's filmography. Acceptance is based on number and accuracy of these aggregated match scores, which can be configured to be more or less tolerant depending on appetite for false matching.

**Known Issues**

1. The notebook assumes that the primary matching entity will have a smaller or equal filmography than the matching set, otherwise scores will be, by median, low. One solution to this is to run comparison A -> B, and then B -> A.

2. Individuals and organisations who were unusually prolific (e.g. [Natalie M. Kalmus](https://en.wikipedia.org/wiki/Natalie_Kalmus)), stand a higher chance of being matched in any context.

3. There is a reasonable chance of confusion between organisations and individuals with similar names and filmographies, e.g. Walt Disney and Walt Disney Studios. Family members or similarly-named partners who frequently collaborate are also susceptible to the same issue.

**License**

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)
