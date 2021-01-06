# JournalPDFScraper

This project was started as a way to find and download free PDFs from medical journals. The goal is to expedite the early parts of medical research where the researcher must search for free PDFs and create a list of paid ones to purchase. With this tool the researcher would simply run the script to identify the free PDFs.

## Status
* As it currently stands, the project is on hiatus due to class work and other projects. The project is not in a finished state and is a work in progress.
* Currently there are a select number of journals that are supported, the tests under `Scrapers>Tests` show which scrapers work as some are still under development.
* I am considering changes to make this more optimized to run on a server and work on more journal websites by using exclusively beautiful soup, rather than selenium. Most jounral webpages make it too much to handle getting to download pages, so this would instead just identify if it is free or not.
