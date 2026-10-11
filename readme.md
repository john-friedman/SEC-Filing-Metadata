# SEC Filing Metadata

SEC endpoints often have the wrong values for SEC filings. Extracted metadata from filings is more reliable.

**data**

(Almost) every SEC filing's extracted metadata converted to columnar format from 1993 to October 10th, 2026. Might be a few thousand missing. I did this on my personal laptop, and exceeded the capacity of my ports in the name of speed.

A full dataset (updated instantly) and queryable with SQL is available on [datamule](https://datamule.xyz/articles/datamule-sec-filings-metadata/).

Note: Before Dec 2025, datamule uses SEC daily archive filings. Slightly different format -- lacks acceptancedatetime.
Note: Sometimes, SEC daily archive filings differ from what ends up on the normal sec.gov that people see. e.g. [normal](https://www.sec.gov/Archives/edgar/data/41023/000004102305000013/0000041023-05-000013.txt) vs [daily archive](https://www.sec.gov/Archives/edgar/Feed/2024/QTR3/). I believe this to be corrections. Not quite sure how this is done. Topic for further investigation.

**motivation**

I oss-ed this repo because [Denis Lima e Alves](https://research-portal.uea.ac.uk/en/persons/denis-lima-e-alves/), mentioned that he had issues with SEC indices misreporting 8-K filings as 10-Ks.

I will add some reports on SEC mismatches here in the future. Not sure if he wants to as well. If this metadata is useful and you (anonymous reader) use it for something, feel free to ping me. I will link to your article.

## Research

See research/