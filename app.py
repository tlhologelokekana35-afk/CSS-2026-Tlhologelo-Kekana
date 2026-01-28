import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Kekana Motjedi Tlhologelo | CV",
    page_icon="📄",
    layout="wide"
)

# Sidebar
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Profile",
        "Experience",
        "Skills",
        "Education",
        "Projects",
        "References"
    ]
)

# Header
st.title("Kekana Motjedi Tlhologelo")
st.subheader("Medical Science | Biotechnology | Biopharmaceutical Research")

st.write(
    """
📍 Cape Town, South Africa  
📞 076 927 6274  
📧 tlhologelokekana35@gmail.com  
"""
)

st.markdown("---")

# Profile Section
if section == "Profile":
    st.header("👤 Professional Profile")
    st.write(
        """
Detail-oriented and results-driven Medical Science graduate with strong laboratory-based
experience in biopharmaceutical manufacturing, molecular biology, and analytical testing.
Skilled in GMP-compliant environments, vaccine production, and pharmaceutical research.
Passionate about innovation, process improvement, and advancing healthcare solutions.
"""
    )

# Experience Section
elif section == "Experience":
    st.header("💼 Professional Experience")

    st.subheader("MassARRAY Intern — Inqaba Biotec")
    st.write("**Duration:** 3 months")
    st.write(
        """
- Nucleic acid extraction and purification from hair and plant tissues  
- RT-PCR setup, execution, and data analysis  
- Operation of mass spectrophotometers  
- Strong laboratory practices, QC, and documentation
"""
    )

    st.subheader("Production Intern — Inqaba Biotec")
    st.write("**Duration:** 3 months")
    st.write(
        """
- Oligonucleotide and probe synthesis using Mermade synthesizer  
- PAGE and cartridge-based purification  
- Workflow management from synthesis to final QC
"""
    )

    st.subheader("Researcher Intern — SAMRC")
    st.write("**Year:** 2024")
    st.write(
        """
- Biopharmaceutical manufacturing training  
- Vaccine production and medical device development  
- Analytical testing: ELISA, PCR, flow cytometry, electrophoresis  
- GMP compliance and documentation management
"""
    )

    st.subheader("CSSFF Studentship Programme — SAMRC")
    st.write("**Year:** 2023")
    st.write(
        """
- Laboratory-based training in vaccine and pharmaceutical manufacturing  
- Bioprocessing, aseptic techniques, QA, and regulatory compliance  
- Strong focus on teamwork and continuous improvement
"""
    )

# Skills Section
elif section == "Skills":
    st.header("🧪 Professional Skills")

    skills = [
        "Upstream & downstream bioprocessing",
        "Aseptic techniques & sterile environments",
        "ELISA, PCR, electrophoresis, flow cytometry",
        "GMP & cleanroom operations",
        "Bioprocessing equipment operation",
        "Laboratory Information Management Systems (LIMS)",
        "Team collaboration & communication",
        "Problem-solving & root cause analysis"
    ]

    for skill in skills:
        st.write(f"✅ {skill}")

# Education Section
elif section == "Education":
    st.header("🎓 Education")

    st.subheader("BSc (Honours) Medical Science in Pharmacology")
    st.write("**Institution:** Sefako Makgatho Health Sciences University")
    st.write("**Status:** Present")

    st.subheader("Bachelor’s Degree in Molecular & Life Sciences")
    st.write("**Majors:** Biotechnology & Biochemistry")
    st.write("**Institution:** University of Limpopo (2022)")

    st.subheader("High School")
    st.write("Harry Oppenheimer High School (2019)")

# Projects Section
elif section == "Projects":
    st.header("🧬 Research Project")

    st.subheader(
        "Development of Antibiotic Oral Medication for Drug-Resistant TB"
    )

    st.write(
        """
This project focuses on developing a liquid formulation of D-cycloserine to improve
treatment adherence and therapeutic outcomes for patients with multidrug-resistant
tuberculosis. The formulation aims to enhance solubility, stability, and ease of
administration, particularly for pediatric and elderly patients.
"""
    )

# References Section
elif section == "References":
    st.header("📞 References")

    st.write(
        """
**Dr Nireshni Chellan**  
Specialist Scientist — SAMRC  
📧 nireshni.chellan@mrc.ac.za  
📞 021 938 0362  

**Dr Pritika Ramharack**  
Senior Scientist — SAMRC  
📧 pritika.ramharack@mrc.ac.za  
📞 021 938 0206  

**Mr A.W.H Mochaki**  
Junior Lecturer — University of Limpopo  
📧 andrew.mochaki@ul.ac.za  
📞 015 268 3251
"""
    )

st.markdown("---")
st.caption("© 2026 Kekana Motjedi Tlhologelo")
