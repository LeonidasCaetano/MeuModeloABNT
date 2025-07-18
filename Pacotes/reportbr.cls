%=========================================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{reportbr}[2014/08/16 Example LaTeX class]

\DeclareOption{booktabs}{\def\@bktbspkg{\RequirePackage{booktabs}}}
\DeclareOption{imakeidx}{\def\@imkidxpkg{\RequirePackage{imakeidx}}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions\relax
\LoadClass{report}

%=========================================================================================
%pacotes
\RequirePackage[english,brazil]{babel}%Pacote BR
%==================================================================
\RequirePackage{mathtools}%equações matematicas
\RequirePackage{amsfonts}%letras matematicas
\RequirePackage{siunitx}\sisetup{detect-all}%Unidades
\RequirePackage{polynom}%divisão polinomial
\RequirePackage{chemfig}%quimica
%==================================================================
\RequirePackage{graphicx}%Inserir imagem
\RequirePackage{xcolor}%cores
%==================================================================
%Tabelas
\RequirePackage{multirow}%multilinha
\RequirePackage{array}%basicão
\RequirePackage{tabularx}%tabela estranha
\RequirePackage{colortbl}%cores
\ifdefined\@bktbspkg \@bktbspkg\fi%solo for py
%==================================================================
\RequirePackage[T1]{fontenc}%acentos
\RequirePackage{indentfirst}%recuo 1º paragrafo
\RequirePackage{parskip}%distancia entre paragrafos
%==================================================================
\RequirePackage{calc}%operação com variaveis
\RequirePackage[section]{placeins}
\RequirePackage{float}%posição absoluta
%==================================================================
\RequirePackage{etoolbox}
\ifdefined\@imkidxpkg \@imkidxpkg\fi
\@ifpackageloaded{imakeidx}{
\makeindex[columns=1, title=ÍNDICE,intoc]
\indexsetup{firstpagestyle=fancy}
\let\addaoindice\index
\renewcommand{\index}[1]{\addaoindice{\MakeTitlecase{#1}}}
}{}
%==================================================================
\ifdefined\directlua
	\RequirePackage{fontspec}%mudar fonte
	\RequirePackage{pdflscape}
	\RequirePackage{luacode}
\fi
\ifdefined\pdfoutput
	\RequirePackage{helvet}
	\renewcommand{\familydefault}{\sfdefault}%Arial
	\RequirePackage{pdflscape}
\fi
\ifdefined\XeTeXversion
	\RequirePackage{mathspec}%mudar fonte
	\RequirePackage{lscape}%pag deitada
\fi
%==================================================================
\RequirePackage{pgffor}%loop option 1 
\RequirePackage{forloop}%loop option 2
%==================================================================
\RequirePackage{appendix}

%=========================================================================================

\RequirePackage[a4paper]{geometry}%Margens e página
\geometry{
	includehead = false,
	includefoot = false,
	twoside 	= false,
	footskip 	= 1cm,
	headheight 	= 2cm,
	headsep 	= 0.5pt,
	top 		= 3cm,
	bottom 		= 2cm,
	left 		= 2cm,
	right 		= 2cm
}


\def\bodygeometry{\newgeometry{
	includehead = false,
	includefoot = false,
	twoside 	= false,
	footskip 	= 1cm,
	headheight 	= 3cm,
	headsep 	= .5cm,
	top 		= 3cm,
	bottom 		= 2cm,
	left 		= 3cm,
	right 		= 2cm
}}

%=========================================================================================

\RequirePackage{caption}%legendas
\DeclareCaptionTextFormat{geraltext}{#1}
\DeclareCaptionLabelFormat{gerallabel}{#1\space#2}
\DeclareCaptionLabelSeparator{geralsep}{:\space}
\DeclareCaptionFont{geralfont}{\footnotesize}
\DeclareCaptionFormat{geralformat}{\bfseries#1#2#3}
\captionsetup{labelformat = gerallabel, textformat = geraltext, labelsep = geralsep, justification = centering, format = geralformat}

%=========================================================================================

\RequirePackage[shortlabels]{enumitem}%listas

\renewcommand{\labelenumi}{\alph{enumi}\hfill)}
\renewcommand{\labelenumii}{--}

\renewcommand{\labelitemi}{\textbullet}
\renewcommand{\labelitemii}{--}

\setlist[itemize,1]{align = left,
	topsep = 0cm,
	itemindent = .5cm+1em,
	leftmargin = 1.5cm, 
	labelwidth = .5cm,
	labelsep = 1em, 
	labelindent = 0cm, 
	listparindent = 0.5cm+1em,
	itemsep = 0cm,
	parsep = \parskip
}

\setlist[enumerate,1]{align = left,
	topsep = 0cm,
	itemindent = .5cm+1em,
	leftmargin = 1.5cm, 
	labelwidth = .5cm,
	labelsep = 1em, 
	labelindent = 0cm, 
	listparindent = 0.5cm+1em,
	itemsep = 0cm,
	parsep = \parskip
}

\setlist[enumerate,2]{align = left,
	topsep = 0cm,
	itemindent = .5cm+1em,  
	leftmargin = 0cm, 
	labelwidth = .5cm,
	labelsep = 1em, 
	labelindent = 0cm, 
	listparindent = 0.5cm+1em,
	itemsep = 0cm,
	parsep = \parskip
}

%=========================================================================================

%novos comandos
%==================================================================
%definemodel
\newcommand{\@titulo}{\ }
\newcommand{\@subtitulo}{}
\newcommand{\@local}{\ }
\newcommand{\@institution}{\ }
\newcommand{\@campus}{\ }

\newcommand{\@autorum}{\ }
\newcommand{\@autordois}{\ }
\newcommand{\@autortres}{\ }
\newcommand{\@autorquatro}{\ }
\newcommand{\@orientador}{\ }
\newcommand{\@coorientador}{\ }

\newcommand{\@nota}{\ }
\newcommand{\@palavraschaves}{\ }
\newcommand{\@epigraphy}{\parbox{10cm}{``I heard a definition of an intellectual, that I thought was very interesting: a man who takes more words than are necessary to tell more than he knows."\par Dwight D. Eisenhower}}
\newcommand{\@dedique}{A família}
\newcommand{\@bancaum}{\ }
\newcommand{\@bancadois}{\ }
%==================================================================
\newcommand{\hyperreftit}{}
\newcommand{\hyperrefsubtit}{}
\newcommand{\hyperrefautum}{}
\newcommand{\hyperrefautdos}{}
\newcommand{\hyperrefauttre}{}
\newcommand{\hyperrefautqua}{}
\newcommand{\hyperrefautores}{{\hyperrefautum\hyperrefautdos\hyperrefauttre\hyperrefautqua}}
\newcommand{\hyperrefkeywords}{}
%==================================================================
\newcommand{\titulo}[1]{\renewcommand{\hyperreftit}{#1}\renewcommand{\@titulo}{#1}}
\newcommand{\subtitulo}[1]{\renewcommand{\hyperrefsubtit}{#1}\renewcommand{\@subtitulo}{\ifstrequal{#1}{}{}{: {#1}}}}
\newcommand{\local}[1]{\renewcommand{\@local}{#1}}
\newcommand{\institution}[1]{\renewcommand{\@institution}{\ifstrequal{#1}{}{\ }{\MakeUppercase{#1}}}}
\newcommand{\campus}[1]{\renewcommand{\@campus}{\ifstrequal{#1}{}{\ }{\MakeUppercase{#1}}}}

\newcommand{\autorum}[1]	{\ifstrequal{#1}{}{}{\renewcommand{\hyperrefautum} {; #1}\renewcommand{\@autorum}{#1}}}
\newcommand{\autordois}[1]	{\ifstrequal{#1}{}{}{\renewcommand{\hyperrefautdos}{; #1}\renewcommand{\@autordois}{#1}}}
\newcommand{\autortres}[1]	{\ifstrequal{#1}{}{}{\renewcommand{\hyperrefauttre}{; #1}\renewcommand{\@autortres}{#1}}}
\newcommand{\autorquatro}[1]{\ifstrequal{#1}{}{}{\renewcommand{\hyperrefautqua}{; #1}\renewcommand{\@autorquatro}{#1}}}
\newcommand{\orientador}[1]	{\renewcommand{\@orientador}{\ifstrequal{#1}{}{\ }{#1}}}
\newcommand{\coorientador}[1]{\renewcommand{\@coorientador}{\ifstrequal{#1}{}{\ }{#1}}}

\newcommand{\nota}[1]{\renewcommand{\@nota}{\ifstrequal{#1}{}{\ }{#1}}}
\newcommand{\palavraschaves}[1]{\renewcommand{\hyperrefkeywords}{{#1}}\renewcommand{\@palavraschaves}{{#1}}}
\newcommand{\epigraphy}[1]{\ifstrequal{#1}{}{}{\renewcommand{\@epigraphy}{\parbox{10cm}{#1}}}}
\newcommand{\dedique}[1]{\ifstrequal{#1}{}{}{\renewcommand{\@dedique}{#1}}}
\newcommand{\banca}[2]{\renewcommand{\@bancaum}{#1}\renewcommand{\@bancadois}{#2}}
%==================================================================
\def\frontpages{
	\begin{titlepage}
		\linespread{1}\selectfont
		\begin{center}
			{\@institution}\par {\@campus}\par 
			\vspace*{2cm}\par
			\@autorum\par \@autordois\par 
			\@autortres\par \@autorquatro\par
			\vspace*{4.3cm}\par
			\textbf{\MakeUppercase\@titulo}\@subtitulo\par
			\vfill \@local\\ \data
		\end{center}
	\end{titlepage}
	\newpage

	\bodygeometry

	\begingroup
		\linespread{1}\selectfont
		\begin{center}
			\@autorum\par \@autordois\par
			\@autortres\par \@autorquatro\par
			\vspace*{8cm} \MakeUppercase{\@titulo}\@subtitulo\par 
			\vspace{1cm}\par
			\hfill \normalsize {\parbox{8cm}{\footnotesize\@nota
			\vspace*{0.5cm}\par
			Orientadora: \@orientador\par
			Coorientador: \@coorientador}}\par
			\vfill	\@local\\ \data
		\end{center}
	\endgroup
	\newpage
}
%==================================================================
\def\printdedicatoria{
	\vspace*{\fill}
	\begin{flushright}
   		\@dedique
	\end{flushright}
}
%==================================================================
\def\printepigraphy{
	\vspace*{\fill}
	\begin{flushright}
		\@epigraphy
	\end{flushright}
}
%==================================================================
%datas
\newcommand{\data}{%
%\ifnum\the\day<10 0\fi\the\day/%
%\ifnum\the\month<10 0\fi\the\month/%
\the\year%
}
%==================================================================
%Fonte
\newcommand{\conteudofonte}{Os autores (\the\year)}
\newcommand{\posfonte}{\centering}

\newcommand{\fonte}[1][\conteudofonte]{

\posfonte
Fonte: #1%
}

%==================================================================
%seção não numerada
\newcommand{\capitulon}[1]{%
\newpage

\phantomsection\label{#1}%
\addcontentsline{toc}{chapter}{\MakeUppercase{#1}}%
\chapter*{#1}%
}
%==================================================================
%seção pre listas
\newcommand{\capitulop}[1]{%
\newpage

\phantomsection\label{#1}%
\chapter*{#1}%
}
%==================================================================
%Tabelas py
\@ifpackageloaded{booktabs}{
	\typeout{Booktabs already loaded}
}{%
	\typeout{Emulating booktabs commands}
	\newcommand{\toprule}{\noalign{\hrule height 2.2pt}}
	\newcommand{\midrule}{\hline}
	\newcommand{\cmidrule}[1]{\cline{#1}}
	\newcommand{\bottomrule}{\noalign{\hrule height 2.2pt}}
}
%==================================================================
%referencias
\newcommand{\makeref}[1]{%
\begingroup
\linespread{1}\selectfont
\chapter{#1}%
\printbibliography[heading=none]%
\endgroup
}
%==================================================================
%sumário
\patchcmd{\tableofcontents}{\@starttoc{toc}}{\label{toc}\@starttoc{toc}}{}{}
\pretocmd{\tableofcontents}{\phantomsection}{}{}
%==================================================================
%Deitada
\ifdefined\pdfoutput
	\newenvironment{deitada}{%
		\newpage%
		\begin{landscape}%
	}{%
		\end{landscape}%
		\newpage%
	}
\fi
%=============================================
\ifdefined\directlua
	\newenvironment{deitada}{%
		\newpage%
		\begin{landscape}%
	}{
		\end{landscape}%
		\newpage%
	}
\fi
%==================================================================
%Formatar usando Lua
\ifdefined\directlua
	\directlua{require("Pacotes/LuaCmds.lua")}
	
	\newcommand{\formatarporcent}[1]{\luaexec{
			tex.sprint(formatar_n_casas(100*#1,2))}\%}

	\newcommand{\formatarinteiro}[1]{\luaexec{
			tex.sprint(formatar_n_casas(#1,0))}}

	\newcommand{\formatarduascasas}[1]{\luaexec{
			tex.sprint(formatar_n_casas(#1,2))}}

	\newcommand{\formatarmoeda}[1]{R\$ \luaexec{
			tex.sprint(formatar_n_casas(#1,2))}}

	\newcommand{\formataroutro}[2]{\luaexec{
			tex.sprint(formatar_n_casas(#1,#2))}}

	\newcommand{\formatartexto}[1]{\luaexec{
			tex.sprint(#1)}}
\fi

%=========================================================================================

\@ifpackageloaded{mathspec}{
	\setmathfont(Digits){Arial}%Latin Modern Math
	\setmathfont(Latin){Arial}%Fira Math
	\setmathfont(Greek){Arial}
	\setmathrm{Arial}
	%aplicar a letras gregas
	\begingroup\lccode`~=`"
		\lowercase{\endgroup
		\everymath{\let~\eu@active@quote}
		\everydisplay{\let~\eu@active@quote}
		}
}{
	%se não for carregado, não há edição
}
\renewcommand{\sin}{\mathop\mathrm{sen}\nolimits}
\renewcommand{\cos}{\mathop\mathrm{cos}\nolimits}
\renewcommand{\tan}{\mathop\mathrm{tg}\nolimits}
\renewcommand{\csc}{\mathop\mathrm{csc}\nolimits}
\renewcommand{\sec}{\mathop\mathrm{sec}\nolimits}
\renewcommand{\cot}{\mathop\mathrm{cotg}\nolimits}
\renewcommand{\arcsin}{\mathop\mathrm{sen}^{-1}\nolimits}
\renewcommand{\arccos}{\mathop\mathrm{cos}^{-1}\nolimits}
\renewcommand{\arctan}{\mathop\mathrm{tg}^{-1}\nolimits}

%=========================================================================================

\pretocmd{\document}{
	\makeatletter
		\@ifpackageloaded{todonotes}{}{
			\def\missingfigure#1{#1}
			\def\todo[#1]#2{}
		}
	\makeatother
	\usepackage[
			linktoc = all,
			hidelinks,
			%draft,
			pdfpagemode=FullScreen,
			pdftitle=\hyperreftit,
			pdfauthor=\hyperrefautores,
			pdfcreator={Leonidas Caetano},
			pdfsubject=\hyperrefsubtit,
			pdfkeywords={\hyperrefkeywords},
			]{hyperref}%links
}{}{\errmessage{Couldn't patch \string\document}}

\ifdefined\chapter \counterwithout{footnote}{chapter}\fi
\renewcommand{\theequation}{\arabic{equation}}

%=========================================================================================