# JournalPDFScraper

This project was started as a way to find and download free PDFs from medical journals. The goal is to expedite the early parts of medical research where the researcher must search for free PDFs and create a list of paid ones to purchase. With this tool the researcher would simply run the script to identify the free PDFs.

As noted in the status below, the project will no longer download PDFs. However, due to the reason listed below, the project will focus on determining if an article is free/paid.

## Status
* The project is undergoing a few fixes to make workable but as it stands I will not be adding any new journals.
* You may notice there is a 'Base.py' and 'BaseSoup.py' file, as well as a 'BMJSoupScraper.py' along with the other scrapers. I intend to change all of these to use beautiful soup when I have time as I don't believe I will be supporting the downloading of files.
  * Note: Downloading files is honestly too hit and miss from journal-to-journal and I really just want the functionality to say if an article is free or not while providing the link.