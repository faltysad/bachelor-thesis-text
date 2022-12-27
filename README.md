# bachelor-thesis-text
Template for typesetting bachelor's / diploma theses at VŠE FIS in LaTeX

	Vilém Sklenák <sklenak@vse.cz>

You can find the basic settings in the file thesis.tex, which also refers to 
other files with individual chapters of the work. Carefully read the main file 
and fill in any missing data. Also add them to the thesis.xmpdata metadata file.

For the translation of the work, pdflatex will probably be the most common. If 
you will be using a separate bibliographic database, a three-step translation of 
pdflatex-biber-pfdlatex is required. However, the template is universal and will 
also be translated by xelatex or lualatex. If you are using xelatex, then you 
need to check the command line to run xelatex:

	xelatex - shell-escape -output-driver="xdvipdfmx -z 0" <filename> 

This setting is important for generating the resulting PDF format according to 
the PDF/A standard.

