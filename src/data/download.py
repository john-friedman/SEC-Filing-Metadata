from datamulehub import sec_filings_archive

# takes a few hours. 
for year in range(1993,2027):
    sec_filings_archive.download_tar(document_type='metadata',filing_date=(f'{year}-01-01',f'{year}-12-31'), max_workers=1000, output_dir=f"metadata/{year}")
