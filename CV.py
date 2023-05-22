import streamlit as st
# import streamlit.components.v1 as components
from PIL import Image
# st.set_page_config(page_title="Manas Sharma", layout='centered')
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Manas Sharma 
##### **(PhD Student)**
''')

image = Image.open('dp.png')
# st.image(image, width=450)
col1, col2, col3 = st.columns([1, 2.5, 1])

with col1:
    st.write(' ')

with col2:
    st.image(image, use_column_width=True)

with col3:
    st.write(' ')
st.write('## Research Interests', unsafe_allow_html=True)
st.info('''
My passion lies in **developing codes and methods** to model the **light-matter interaction of hybrid systems**. More specifically, I am working on improving and accelerating **quantum embedding** techniques for molecular and periodic systems. 
A core focus of my Ph.D. has been on implementing **density functional theory (DFT) based embedding techniques** and coupling them to real time-time dependent DFT (**RT-TDDFT**) and wavefunction theory (**WFT**) methods. 
Most notably, I was able to calculate the excitation energies of solvated molecules and adsorption energies of **molecule-periodic** systems using **WFT-in-DFT** method at only a fraction of cost of a traditional calculation.
More recently, my work has been focused on accurate molecule-in-periodic embedding and high harmonic generation via RT-TDDFT. 
Recently, I have also started taking interest in **deep learning** and created a performant neural network library from scratch which supports parallelization and GPUs. 
I am also experienced in creating GUIs for material modeling, visualizations and input file creations.

Besides all this, I love making [YouTube tutorials](https://www.youtube.com/c/Bragitoff_physics), web & [Android apps](https://play.google.com/store/apps/developer?id=Manas+Sharma), and computer software/[libraries](https://github.com/manassharma07) for researchers and students.
''')

#####################
# Navigation
st.markdown('''
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.6/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
''', unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
# st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown('''
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.6/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
''', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.bragitoff.com/about/" target="_blank">Manas Sharma</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavNew" aria-controls="navbarNavNew" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavNew">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#news">News</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#about">About</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.bragitoff.com/">Blog</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.youtube.com/c/Bragitoff_physics">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#code-development">Code Dev</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#selected-publications">Publications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#conferences-workshops-and-seminars">Conferences</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Contact</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/manassharma07/resume/blob/main/Manas_Sharma_CV.pdf">CV PDF</a>
      </li>
    </ul>
  </div>
</nav>

""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    # st.markdown(f'`{a}`')
    st.markdown(f'<b style="color:#c95593;font-size:16px;">{a}</b>', unsafe_allow_html=True)
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    # st.markdown(f'`{a}`')
    st.markdown(f'<b style="color:#c95593;font-size:16px;">{a}</b>', unsafe_allow_html=True)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

######################
## NEWS #############
st.markdown('''
## News
''')
txt('Published a collaborative [article](https://onlinelibrary.wiley.com/doi/full/10.1002/adom.202203070) with experimental groups on harmonic generation in [Advanced Optical Materials](https://onlinelibrary.wiley.com/page/journal/21951071/homepage/productinformation.html)','22 May 2023')
txt('Published a big part of my PhD work as an [article](https://doi.org/10.1021/acs.jctc.2c00380) in [JCTC](https://pubs.acs.org/doi/10.1021/acs.jctc.2c00380)','12 Oct 2022')
txt('Presented a [poster](https://www.bragitoff.com/2022/09/biovia-conference-2022-poster-wavefunction-in-dft-embedding-for-molecular-and-periodic-systems/) at [BIOVIA Conference 2022](https://events.3ds.com/biovia-conference-2022)','11 Oct 2022')
txt('Presented a [poster](https://www.bragitoff.com/2022/09/icqnn-2022-poster-density-functional-theory-based-embedding-for-molecular-and-periodic-systems/) at [ICQNN 2022](https://www.noa.uni-jena.de/international-conference-of-quantum-nonlinear-and-nanophotonics-2022) in Jena, Germany','8 Sep 2022')
txt('Presented a [poster](https://www.bragitoff.com/2022/08/psik-2022-poster-dft-based-embedding/) at [PsiK 2022](https://www.psik2022.net/) in Lausanne, Switzerland','23 Aug 2022')
txt('Released [ONLINE DEMO](https://www.bragitoff.com/2022/11/crysx-demo-dft-based-embedding/) of Frozen Density Embedding and Projection Based Embedding','15 Aug 2022')
txt('Released CompChem Chemical File Format Converter [Web App](https://www.bragitoff.com/2022/08/crysx-compchem-file-converter-web-app/)','11 Aug 2022')
txt('Gave a talk at [ETSF 2022](https://workshop.etsf.eu/) held at [imec](https://www.imec-int.com/en) in Leuven, Belgium','14 Jun 2022')
txt('Released Basis Set Converter [Web App](https://www.bragitoff.com/2022/04/basis-set-converter-web-app/)','18 Apr 2022')
txt('Presented my contributions in TURBOMOLE at the TURBOMOLE developers seminar series','22 Feb 2022')

######################
## About #############
st.markdown('''
## About
''')
st.markdown('''
I am a fourth-year PhD student in Physics at Friedrich Schiller University of Jena (FSU) Germany, fortunate to be advised by [Prof. Marek Sierka](https://www.cmsg.uni-jena.de/).

I possess strong verbal, presentation and written communication skills as demonstrated by extensive **participation in `>16` conferences (`7` talks; `9` posters)** as well as publishing **`6` research articles**.

Prior to joining FSU, I obtained a Master's in Physics from University of Delhi (India), where I worked with [Dr. Debabrata Mishra](https://scholar.google.com/citations?user=-vujB0AAAAAJ&hl=en). I published two papers with him.  
I obtained my Bachelor's in Physics (Hons) from the University of Delhi as well. 
I am originally from a small, but beautiful town Haldwani, a few minutes from Nainital in India.
''')



# LONG_TEXT = '''ssss
# sss
# ss
# ss
# s
# s
# s
# s
# s
# s
# s
# s'''
# components.html(f"<pre>{LONG_TEXT}</pre>", height=600)

####################
st.markdown('''
## Education
''')

# txt('**Doctor of Philosophy** (Medical Technology), *Mahidol University*, Thailand',
# '2002-2006')
# st.markdown('''
# - GPA: `3.89`
# - Research thesis entitled `Computer-aided molecular design for biological and chemical applications : Quantum chemical and machine learning approach`.
# - Received Royal Golden Jubilee Ph.D. Scholarship of `2.152 million THB` covering tuition and stipend.
# - Thesis awarded `1st` Prize by the National Research Council of Thailand.
# ''')
txt('**PhD candidate** Physics, *Friedrich Schiller University Jena*, Jena, Germany',
'2019-present')
txt('**Master of Science** Physics, *University of Delhi*, New Delhi, India',
'2016-2018')
# st.markdown('''
# - Average: `87.5%`
# - Ranked second in my College.
# ''')
txt('**Bachelor of Science** (Hons) Physics, *University of Delhi*, New Delhi, India',
'2013-2016')
# st.markdown('''
# - Average: `87.5%`
# - Ranked second in my College.
# ''')

#####################
# st.markdown('''
# ## Work Experience
# ''')

# txt('**Head, Center of Data Mining and Biomedical Informatics**, Faculty of Medical Technology, Mahidol University, Thailand',
# '2011-2021')
# st.markdown('''
# - Managing a Center of `10` professors, researchers and students to ensure KPIs are strategically achieved namely to publish at least `20+` research publications annually. 
# - Actively took part in the talent hiring process as well as help employees to plan and develop their career path.
# - Set budget and handle procurement in order to facilitate education and research activities. Secured `> 10 million THB` budget.
# - Set and reflect on OKR on an annual basis to ensure productivity strategically matches the organization's direction.
# ''')

# txt('**Associate Professor**, Faculty of Medical Technology, Mahidol University, Thailand',
# '2012-2021')
# txt('**Assistant Professor**, Faculty of Medical Technology, Mahidol University, Thailand',
# '2009-2012')
# txt('**Lecturer**, Faculty of Medical Technology, Mahidol University, Thailand',
# '2006-2009')
# st.markdown('''
# - Provided mentorship and supervision to junior faculty, researchers, Ph.D./M.Sc./B.Sc. students. Mentored `3` Post-doctoral fellows, supervised `13` Ph.D. students, supervised `8` M.Sc. students, supervised `13` B.Sc. students and hosted `6` visiting students from U.S., Sweden and India.
# - Wrote and applied for research grants. Served as Principal Investigator for research grants that have been awarded `12.5 million THB` and `1.117 million SEK` in research funding from Thai and Swedish grant agencies.
# - Conducted research by applying machine learning to computational drug discovery and ensuring that research output exceeds `20+` articles per year.
# - Taught `10+` undergraduate/graduate classes on Bioinformatics, Data Mining, Scientific Research and Presentation, Research Methodology, Graduate Seminar, Programming for Health Data Science, etc.
# - Peer reviewed `100+` research articles for leading scientific journals.
# ''')

# txt('**Co-Chair**, International Conference on Pharmaceutical Bioinformatics at Pattaya, Thailand',
# '2016')
# st.markdown('''
# - Oversee all aspects of the conference preparations from conception to launch. This include inviting keynote and plenary speakers, create advertisement flyers, create abstract book, etc.
# - Conference attracted `200+` participants from `40+` countries from university and industry sector.
# - Chaired keynote session, technical workshop and some of the parallel sessions.
# ''')

# txt('**Content Creator**, [Data Professor YouTube Channel](https://youtube.com/dataprofessor/)',
# '2019-Present')
# st.markdown('''
# - `100,000+` subscribers on YouTube
# - Created `261` educational videos on data science, machine learning and bioinformatics as well as hosted several podcast episodes with data scientists.
# - Created `3` sponsored videos for Notion, Gradio and Classpert.
# ''')

# txt('**Content Creator**, [Coding Professor YouTube Channel](https://youtube.com/codingprofessor/)',
# '2019-Present')
# st.markdown('''
# - `3,200+` subscribers on YouTube
# - Created `38` educational videos on Python and R programming.
# ''')

# txt('**Technical Writer**, [Data Professor Blog](https://data-professor.medium.com/) on Medium.com',
# '2019-Present')
# st.markdown('''
# - `4,100+` subscribers on Medium
# - Written `68` technical blogs on data science, machine learning and bioinformatics.
# ''')

#####################
st.markdown('''
## Code development
''')
st.write('#### Contributions')
txt4('TURBOMOLE', 'DFT based embedding coupled with WFT and RT-TDDFT methods within the RIPER module of the popular TURBOMOLE package', 'https://www.turbomole.org/')
st.write('#### Independently developed software')
txt4('CrysX-NN', 'An efficient neural network library from scratch that supports parallelization and GPUs', 'https://github.com/manassharma07/crysx_nn')
txt4('CrysX-3D Viewer', 'A molecule and crystal viewer that renders high quality visualizations using complex shaders developed using Unity gaming engine. Avaliable on Android, Windows, Mac and Linux','https://www.bragitoff.com/crysx-3d-viewer/')
txt4('CrysX-AR', 'An Android app for augmented reality visualization of molecules and crystals', 'https://play.google.com/store/apps/details?id=com.bragitoff.crysxar')
txt4('CrysX-Crystallographic Tools', 'A set of crystallographic tools available as an Android app ','https://play.google.com/store/apps/details?id=com.bragitoff.powderdiffractionsimulator')
st.write('#### Web Apps, Tools and Other Projects')
txt4('CrysX-Demo DFT based Embedding', 'Online demo of frozen density embedding and projection based embedding', 'https://www.bragitoff.com/2022/09/crysx-demo-dft-based-embedding/')
txt4('CrysX-CompChem File Converter', 'Web app that allows inter-conversion between various chemical file formats in current use', 'https://www.bragitoff.com/2022/08/crysx-compchem-file-converter-web-app/')
txt4('Basis Set Converter', 'Web app to inter-convert between various basis set formats', 'https://www.bragitoff.com/2022/04/basis-set-converter-web-app/')
txt4('The Math App', 'A suite of mathematical tools that has the potential to act as a substitute for Computer softwares like Matlab/Scilab on Android devices', 'https://play.google.com/store/apps/details?id=com.bragitoff.themathapp&hl=en_US&gl=US')
txt4('ML: Microstructure Classification Demo', 'A web demo app of a neural network (crysx_nn) model trained to classify microstutures', 'https://www.bragitoff.com/2022/02/microstructure-classification-using-neural-networks-streamlit-app/')
txt4('ML: MNIST_Plus Digit Classification Demo', 'A web app that classifies user given handwritten digits using a convolutional network model (PyTorch) trained on a modified MNIST dataset', 'https://www.bragitoff.com/2022/01/digit-recognition-app-streamlit-trained-on-the-mnist_plus-dataset-using-pytorch-cnn-model/')



#####################
st.markdown('''
## Selected Publications
''')
st.write('Here is a link to my [Google Scholar](https://scholar.google.com/citations?user=WYOEL94AAAAJ&hl=en)')
# txt('','')
txt('''W. Li, A. Saleh, **M. Sharma**, C. Huenecke, M. Sierka, M. Neuhaus, L. Hedewig, B. Bergues, M. Alharbi, H. ALQahtani, A. M. Azeer, S. Graefe, M.
F. Kling, A. F. Alharbi, and Z. Wang [*Resonance Effect in Brunel Harmonic Generation in Thin Film Organic Semiconductors*](https://onlinelibrary.wiley.com/doi/full/10.1002/adom.202203070)',
**Adv. Optical Mater.** 2203070 ''', '22 May **2023**')
txt('''**M. Sharma**, and M. Sierka [*Efficient Implementation of Density Functional Theory based Embedding for Molecular and Periodic Systems using Gaussian Basis Functions*](https://pubs.acs.org/doi/10.1021/acs.jctc.2c00380)',
**J. Chem. Theo. Comput.** 18, 11, 6892-6904 ***[ON SUPPLEMENTARY COVER🔖]***''', '12 Oct **2022**')
txt('''C. Mueller, **M. Sharma**, and M. Sierka,
[*Real-time time-dependent density functional theory using density fitting and the continuous fast multipole method*](https://onlinelibrary.wiley.com/doi/full/10.1002/jcc.26412),
**J Comput Chem.** 41: 2573–2582. ''','10 Sep **2020**')
txt('''**M. Sharma**, and D. Mishra,
[*CrysX: crystallographic tools for the Android platform*](https://onlinelibrary.wiley.com/iucr/doi/10.1107/S1600576719013682),
**J. Appl. Cryst.** 52, 1449-1454 ***[ON COVER PAGE🔖]*** ''','31 Oct **2019**')
txt('''**M. Sharma**, and D. Mishra,
[*DFT+U study of small ZnO nanoclusters*](https://aip.scitation.org/doi/abs/10.1063/1.5122485),
**AIP Conference Proceedings** 2142, 110025 ''','29 Aug **2019**')
txt('''**M. Sharma**, D. Mishra, and J. Kumar,
[*First-principles study of the structural and electronic properties of bulk ZnS and small ZnnSn nanoclusters in the framework of the DFT+U method*](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.100.045151),
**Phys. Rev. B** 100, 045151''','31 Jul **2019**')


#####################
st.markdown('''
## Conferences, Workshops and Seminars
''')
txt4('Talk', 'VISTA Seminars 2022 (VIRTUAL ([link](https://quantum-dynamics-hub.github.io/VISTA/))', '30 Nov 2022')
txt4('Poster [🔗](https://www.bragitoff.com/2022/09/biovia-conference-2022-poster-wavefunction-in-dft-embedding-for-molecular-and-periodic-systems/)', 'BIOVIA Conference 2022 (VIRTUAL ([link](https://events.3ds.com/biovia-conference-2022))', '11-13 Oct 2022')
txt4('Poster [🔗](https://www.bragitoff.com/2022/09/icqnn-2022-poster-density-functional-theory-based-embedding-for-molecular-and-periodic-systems/)', 'ICQNN 2022 Conference in Jena, Germany ([link](https://www.noa.uni-jena.de/international-conference-of-quantum-nonlinear-and-nanophotonics-2022))', '05-09 Sep 2022')
txt4('Poster [🔗](https://www.bragitoff.com/2022/08/psik-2022-poster-dft-based-embedding/)', 'Psi-K 2022 Conference at EPFL in Lasuanne, Switzerland ([link](https://www.psik2022.net/))', '22-25 Aug 2022')
txt4('Talk [🔗](https://youtu.be/PEU5y_BQp1k)', '25th ETSF Workshop on Electronic Excitations 2022 in Leuven, Belgium ([link](https://workshop.etsf.eu/))', '13-17 Jun 2022')
txt4('Poster [🔗]()', '~~12th Triennial Congress of the World Association of Theoretical and Computational Chemists (WATOC 2022) in Vancouver, Canada~~***Could not attend due to VISA issue :(***', '3–8 Jul 2022')
txt4('Talk [🔗](https://youtu.be/Brsi9O_Jqfk)', 'Turbomole Developers Seminar Series 2021-2022', '21 Feb 2022')
txt4('Talk', 'NOA Spring Meeting 2022 (ONLINE) ([link](https://www.noa.uni-jena.de/news-events/see-the-agenda-of-2022-spring-meeting))', '21-23 Feb 2022')
txt4('Talk', 'Computational Methods in Materials Science (CMMS 2021) (ONLINE) ([link](https://cmms2021.ptbm.pl/))', '24-25 Sep 2021')
txt4('Poster', '57th Symposium on Theoretical Chemistry (STC 2021) (ONLINE) ([link](https://stc2021.uni-wuerzburg.de/))', '20-24 Sep 2021')
txt4('Talk [🔗](https://youtu.be/sL4CjVVVw9o)','EMRS Fall 2021 meeting (Online) ***BEST ORAL PRESENTATION AWARD 🏆*** ([link](https://www.european-mrs.com/meetings/2021-fall-meeting))','20-23 Sep 2021')
txt4('Talk [🔗](https://youtu.be/2xllcGJiO-M)', 'The Materials and Molecular Modelling Hub++ Annual Conference 2021 (ONLINE) ([link](https://mmmhub.ac.uk/mmm-hub-conference-2021/))', '14-15 Sep 2021')
txt4('Talk [🔗](https://youtu.be/_r1IiEpfKTw)', 'DokDok Lite 2021 in Jena, Germany ([link](https://www.asp.uni-jena.de/doctoral-phd/former-events/dokdok-lite-2021))', '01-03 Sep 2021')
txt4('Poster', 'International Workshop on Recent Developments in Electronic Structure (ES21) (ONLINE) ([link](https://www.simonsfoundation.org/international-workshop-on-recent-developments-in-electronic-structure-es21/))', '12-15 Jul 2021')
txt4('Poster','eSSENCE-eMMC eMeeting MMMM 2021 (Online) ([link](https://sites.google.com/view/emultiscale2021/home))','07-08 Jun 2021')
txt4('Attended','International Workshop on Computer-Aided Materials Discovery (Weekly Online ZOOM Webinars) ([link](https://www.materialssquare.com/workshop))','27 May-24 Jun 2021')
txt4('Presentation','NOA CRC 1375 Spring Meeting (ONLINE) ','15‐17 Feb 2021')
txt4('Attended','Intel® Software Development Tools for HPC (Webinar) ([link](https://indico.tpi.uni-jena.de/event/146/))','11-20 Nov 2020')
txt4('Attended','Intel® Software Development Tools for Artificial Intelligence (Webinar) ([link](https://indico.tpi.uni-jena.de/event/147/))','17 Nov 2020')
txt4('Attended','NOA Fall PhD School (ONLINE) ([link](https://indico.tpi.uni-jena.de/event/144/timetable/))','26-28 Oct 2020')
txt4('Poster + Presentation','NOA Spring School and PI Workshop in Jena, Germany ([link](https://www.noa.uni-jena.de/news+_+events/1st+noa+spring+school+and+pi+workshop_+2-6+march+2020))','02-06 Mar 2020')
txt4('Attended','NOA seminar by Dr. Heiko Appel (MPI Hamburg) in Jena, Germany ([link](https://www.noa.uni-jena.de/news+_+events/21+january+2020_+noa+seminar+by+dr_+heiko+appel+(mpi+hamburg)))','21 Jan 2020')
txt4('Attended','24th ETSF Workshop on Electronic Excitations in Jena, Germany ([link](https://workshop.etsf.eu/))','16-20 Sep 2019')
txt4('Poster','ICABS 2019 in Bhiwani, India ([link](http://www.icabs19.com/))','07-09 Feb 2019')
txt4('Poster','6th ISIF 2017 in New Delhi, India ([link](http://www.meetingsnmore.com/isif%202017/))','13 Dec 2017')



# #####################
st.markdown('''
## Skills
''')
txt3('Programming languages', '`C`,  `C++`, `C#`, `Python`, `FORTRAN`, `Java`, `shell scripting`')
txt3('DFT methods development', '`PySCF`,  `TURBOMOLE`')
txt3('DFT / Quantum Chemistry packages', '`Quantum ESPRESSO`, `PySCF`,  `TURBOMOLE`, `NWChem`, `Serenity`')
txt3('Chemical system/material modeling and visualizations/animations', '`VESTA`, `Avogadro`,  `Jmol`, `VMD`, `CrysX-3D Viewer`, `BURAI`, `Py3Dmol`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`, `PyTorch`, `CrysX-NN`')
txt3('App development', '`Android`, `Windows`')
txt3('Web development', '`Wordpress`, `HTML`')
txt3('Web app development', '`Streamlit`')
txt3('Data processing/wrangling', '`pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`')
txt3('Outreach', '[`YouTube videos`](https://www.youtube.com/c/Bragitoff_physics), [`Blog posts`](https://bragitoff.com), [`Instagram posts`](https://www.instagram.com/___physwhiz___)')
txt3('Debugging and profiling','`ARM forge for FORTRAN`, `VS code for python`')
txt3('Miscellaneous','`Video editing`, `Molecular animations`,`Graphic designing`, `Photo editing`')



#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/manassharma07')
txt2('Blog', 'https://bragitoff.com')
txt2('YouTube', 'https://www.youtube.com/c/Bragitoff_physics')
txt2('Twitter', 'https://twitter.com/manassharma07')
txt2('GitHub', 'https://github.com/manassharma07/')
txt2('Instagram', '[https://www.instagram.com/___physwhiz___](https://www.instagram.com/___physwhiz___)')
txt2('•', 'https://www.instagram.com/ducktape07/')
txt2('•', 'https://www.instagram.com/crysx_3d/')
txt2('Facebook', 'https://www.facebook.com/ducktape07')
txt2('•', 'https://www.facebook.com/bragitoff/')
txt2('•', 'https://www.facebook.com/physwhizforum/')
txt2('ORCID', 'https://orcid.org/0000-0002-5346-6280')
txt2('Google Scholar', 'https://scholar.google.com/citations?user=WYOEL94AAAAJ&hl=en')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Manas-Sharma-5')

