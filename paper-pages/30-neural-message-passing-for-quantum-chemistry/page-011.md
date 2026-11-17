---
type: Research Paper Chunk
chunk_type: page
paper: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
source: ../../papers/30-neural-message-passing-for-quantum-chemistry.md
paper_title: Neural Message Passing for Quantum Chemistry
sequence: 30
page: 11
pages: [11]
page_of: 14
topics: ["../../topics/graph-neural-networks.md", "../../topics/relational-reasoning.md"]
description: "Neural Message Passing for Quantum Chemistry • Free energy of atomization G (eV): Once again this is similar to U and H, but assumes that the system…"
status: stable
generated: { by: tools/build_chunks.py, at: 2026-11-17T16:30:00Z }
---

# Page 11 of 14 - Neural Message Passing for Quantum Chemistry

> Page 11 of the source PDF, verbatim as extracted. Canonical document: [30 - Neural Message Passing for Quantum Chemistry](../../papers/30-neural-message-passing-for-quantum-chemistry.md)

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

## 10.3. Chemical Accuracy and DFT Error

• Lowest Unoccupied Molecular Orbital (LUMO) εLUMO (eV): Like HOMO, LUMO is the lowest energy electronic state that is unoccupied.

In Table 5 we list the mean absolute error numbers for chemical accuracy. These are the numbers used to compute the error ratios of all models in the tables. The mean absolute errors of our models can thus be calculated as (Error Ratio) × (Chemical Accuracy). We also include some estimates of the mean absolute error for the DFT calculation to the ground truth. Both the estimates of chemical accruacy and DFT error were provided in Faber et al. (2017).

• Electron energy gap ∆ε (eV): This is the difference in energy between LUMO and HOMO. It is the lowest energy transition that can occur when an electron is excited from an occupied state to an unoccupied state. ∆ε also dictates the longest wavelength of light that the molecule can absorb.

Finally, there are several measures of the spatial distribution of electrons in the molecule:

## 10.4. Additional Results

In Table 6 we compare the performance of the best architecture (edge network + set2set output) on different sized training sets. It is surprising how data efficient this model is on some targets. For example, on both R2 and Omega our models are equal or better with 11k samples than the best baseline is with 110k samples.

• Electronic Spatial Extent ⟨R2⟩(Bohr2): The electronic spatial extent is the second moment of the charge distribution, ρ(r), or in other words ⟨R2⟩= R

drr2ρ(r).

• Norm of the dipole moment µ (Debye): The dipole moment, p(r) =

dr′p(r′)(r −r′), approximates the electric field far from a molecule. The norm of the dipole moment is related to how anisotropically

R

In Table 7 we compare the performance of several models trained without spatial information. The left 4 columns show the results of 4 experiments, one where we train the

---

[previous page](page-010.md) · [next page](page-012.md) · [all pages](index.md)
