"""Pipeline wrapper for the sentence classification model.

"""
import nltk
nltk.download('punkt')

from claim import get_claim


# This is the string that we will classify         
abstract = """
Because of their contractile activity and their high oxygen consumption and metabolic rate, skeletal muscles continually produce moderate levels of reactive oxygen and nitrogen species (ROS/RNS), which increase during exercise and are buffered by multiple antioxidant systems to maintain redox homeostasis. Imbalance between ROS/RNS production and elimination results in oxidative stress (OxS), which has been implicated in ageing and in numerous human diseases, including cancer, diabetes or age-related muscle loss (sarcopenia). The study of redox homeostasis in muscle was hindered by its lability, by the many factors influencing technical OxS measures and by ROS/RNS important roles in signaling pathways and adaptative responses to muscle contraction and effort, which make it difficult to define a threshold between physiological signaling and pathological conditions. In the last years, new tools have been developed that facilitate the study of these key mechanisms, and deregulation of redox homeostasis has emerged as a key pathogenic mechanism and potential therapeutic target in muscle conditions. This is in particular the case for early-onset myopathies, genetic muscle diseases which present from birth or early childhood with muscle weakness interfering with ambulation and often with cardiac or respiratory failure leading to premature death. Inherited defects of the reductase selenoprotein N in SEPN1-related myopathy leads to chronic OxS of monogenic origin as a primary disease pathomechanism. In myopathies associated with mutations of the genes encoding the calcium channel RyR1, the extracellular matrix protein collagen VI or the sarcolemmal protein dystrophin (Duchenne Muscular Dystrophy), OxS has been identified as a relevant secondary pathophysiological mechanism. OxS being drug-targetable, it represents an interesting therapeutic target for these incurable conditions, and following preclinical correction of the cell or animal model phenotype, the first clinical trials with the antioxidants N-acetylcysteine (SEPN1- and RYR1-related myopathies) or epigallocatechin-gallate (DMD) have been launched recently. In this review, we provide an overview of the mechanisms involved in redox regulation in skeletal muscle, the technical tools available to measure redox homeostasis in muscle cells, the bases of OxS as a primary or secondary pathomechanism in early-onset myopathies and the innovative clinical trials with antioxidants which are currently in progress for these so-far untreatable infantile muscle diseases. Progress in our knowledge of redox homeostasis defects in these rare muscle conditions may be useful as a model paradigm to understand and treat other conditions in which OxS is involved, including prevalent conditions with major socioeconomic impact such as insulin resistance, cachexia, obesity, sarcopenia or ageing."""

# removing unnecessary punctuation because problems in tokenization
punctuation = '!"#$%&\'()*+-/:;?@[\]^_`{|}~'

for c in punctuation:
  if c in abstract:
    abstract = abstract.replace(c, ' ')   