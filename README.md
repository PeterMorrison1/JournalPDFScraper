# JournalPDFScraper

This project was started as a way to find and download free PDFs from medical journals. The goal is to expedite the early parts of medical research where the researcher must search for free PDFs and create a list of paid ones to purchase. With this tool the researcher would simply run the script to identify the free PDFs.

As noted in the status below, the project will no longer download PDFs. However, due to the reason listed below, the project will focus on determining if an article is free/paid.

## Status
* The project is undergoing a few fixes to make workable but as it stands I will not be adding any new journals.
* You may notice there is a 'Base.py' and 'BaseSoup.py' file, as well as a 'BMJSoupScraper.py' along with the other scrapers. Some of the websites are unable to use beautifulsoup as they use Javascript to load content after or require a button to be clicked to load content. I decided to keep both as Beautifulsoup is significantly faster in the cases where it can be used.
* Note: Downloading files is honestly too hit and miss from journal-to-journal and I really just want the functionality to say if an article is free or not while providing the link. I don't want to add any burden to journal websites, so I am keeping this to checking and not downloading. If APIs are released in the future I may alter this.


## Contributing
If anyone wishes to add more journals I would greatly appreciate it. The existing scraper files can essentially be copied and alter the classes/elements/ids used and the methods called from the parent classes. Generally, if a journal website only says 'free' on free articles then you just need to check if that element exists. Then add the new scraper to the list of scrapers in JournalScraper.py.
