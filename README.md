# simple-text-extraction
Executable that when run will traverse a folder, extract text for all files, and create a subfolder with text files. During text extraction process a new command prompt will display with the that is file currently being processed.

## Instructions
Create a folder for all of the files that need to have text extracted. Run *bulk_text_extraction.exe* in the dist folder. A file explorer prompt will display - select the folder where your files are stored. A subfolder called **output** will be created with all of the extracted text.

## Notice
Includes latest version of [Apache Tika](https://www.apache.org/licenses/LICENSE-2.0) which allows text/metadata extraction for 1000+ file types. Executable packaged with pyinstaller and only tested on Windows.