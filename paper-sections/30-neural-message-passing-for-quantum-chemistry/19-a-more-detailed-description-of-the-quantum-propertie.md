---
type: Research Paper Chunk
chunk_type: semantic-section
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
section: 10.2. A More Detailed Description of the Quantum Properties
section_role: other
section_index: 19
pages: [10, 11]
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "˜Lv,w,i,jxw,i yv,j = σ   i=1,w=1 First there the four atomization energies. N X ! ˜Lv,wxw yv = σ . • Atomization energy at 0K U0 (eV): This is the…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# 10.2. A More Detailed Description of the Quantum Properties

> Section 19 of 21 from [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · `other` · pages 10-11

˜Lv,w,i,jxw,i

yv,j = σ





i=1,w=1

First there the four atomization energies.

N X

!

˜Lv,wxw

yv = σ

.

• Atomization energy at 0K U0 (eV): This is the energy required to break up the molecule into all of its constituent atoms if the molecule is at absolute zero. This calculation assumes that the molecules are held at fixed volume.

w=1

Relabelling yv as ht+1

v and xw as ht

w this last line can be interpreted as the message passing update in an MPNN where M(ht

w) = ˜Lv,wht

v, ht

w and U(ht

v, mt+1

v ) = σ(mt+1

v ).

• Atomization energy at room temperature U (eV): Like U0, this is the energy required to break up the molecule if it is at room temperature.

10.1.1. THE SPECIAL CASE OF KIPF AND WELLING (2016)

• Enthalpy of atomization at room temperature H (eV): The enthalpy of atomization is similar in spirit to the energy of atomization, U. However, unlike the energy this calculation assumes that the constituent molecules are held at fixed pressure.

Motivated as a first order approximation of the graph laplacian methods, Kipf & Welling (2016) propose the following layer-wise propagation rule:

˜D−1/2 ˜A ˜D−1/2HlW l

Hl+1 = σ

(7)

## Neural Message Passing for Quantum Chemistry

• Free energy of atomization G (eV): Once again this is similar to U and H, but assumes that the system is held at fixed temperature and pressure during the dissociation.

Table 5. Chemical Accuracy For Each Target Target DFT Error Chemical Accuracy mu .1 .1 alpha .4 .1 HOMO 2.0 .043 LUMO 2.6 .043 gap 1.2 .043 R2 1.2 ZPVE .0097 .0012 U0 .1 .043 U .1 .043 H .1 .043 G .1 .043 Cv .34 .050 Omega 28 10.0

Next there are properties related to fundamental vibrations of the molecule:

• Highest fundamental vibrational frequency ω1 (cm−1): Every molecule has fundamental vibrational modes that it can naturally oscillate at. ω1 is the mode that requires the most energy.

• Zero Point Vibrational Energy (ZPVE) (eV): Even at zero temperature quantum mechanical uncertainty implies that atoms vibrate. This is known as the zero point vibrational energy and can be calculated once the allowed vibrational modes of a molecule are known.

the charge is distributed (and hence the strength of the field far from the molecule). This degree of anisotropy is in turn related to a number of material properties (for example hydrogen bonding in water causes the dipole moment to be large which has a large effect on dynamics and surface tension).

Additionally, there are a number of properties that concern the states of the electrons in the molecule:

• Highest Occupied Molecular Orbital (HOMO) εHOMO (eV): Quantum mechanics dictates that the allowed states that electrons can occupy in a molecule are discrete. The Pauli exclusion principle states that no two electrons may occupy the same state. At zero temperature, therefore, electrons stack in states from lowest energy to highest energy. HOMO is the energy of the highest occupied electronic state.

• Norm of the static polarizability α (Bohr3): α measures the extent to which a molecule can spontaneously incur a dipole moment in response to an external field. This is in turn related to the degree to which i.e. Van der Waals interactions play a role in the dynamics of the medium.

---

Full document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md) · Page-level evidence: [paper-pages/30-neural-message-passing-for-quantum-chemistry](../../paper-pages/30-neural-message-passing-for-quantum-chemistry/index.md)
