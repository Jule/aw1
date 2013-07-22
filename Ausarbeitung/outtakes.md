# Intro

As modern embedded applications evolve, their performance requirements increase. Due to the limitations of embedded platforms, such as constraints in power consumption and heat dissipation, these increased performance requirements cannot be met by increasing processor clock rates.

Consequently, modern embedded platforms increasingly feature more than a single processing core, thus offering high-performance computing capabilities, while preservering low-power consumption constraints <!--\citep{Wang2013}-->.

The goal is to get a broad overview of the state-of-the-art techniques being used, as well as their up- and downsides, especially in resource-constrained environments.


# Techniques

that operate on multiple data simultaneously (i.e. in parallel), namely "Single instruction, multiple data" (SIMD) and "Multiple instruction, multiple data" (MIMD). This categorization is often called Flynn's Taxonomy, which also describes


## MIMD

include multiprocessor systems, and as such are almost universally available in todays desktop computers, and increasingly available on embedded platforms. Furthermore, many modern multi-core microprocessors feature SIMD subsystems, such as Intel's SSE extensions, and

# Stuff that provides parallelism

* E.g. on a relatively high level, one can use threads
* But there are also things like GPUs, SIMD etc


# Pipeline pattern

The pipeline concept consists of taking a sequential problem, such as the application of several image filters to a sequence of source images, and dividing this sequential process into so-called "stages". As an example, there is a four filter sequence depicted in <!--\autoref{fig:image-pipeline}-->, where the first step is resizing the image, the next step is to convert it to grayscale, etc. Naturally, it is not possible to perform the histogram equalization at the same time as the perspective correction, since the latter has to be applied to the already equalized image.

By dividing the sequential application of the filters into stages that each apply a single filter,


# Go
## Comparison to C

<!--\todoin{Syntactical/Semantical differences as well as performance comparisons, if possible. Context switch time, garbage collection impact, plain performance (e.g. loops) compared to C, all that stuff.}-->

# Gliederungshinweise


* Einleitung
    * Thema und dessen Anwendungsfeld bzw. dessen perspektivische Nutzung zur Unterstützung der Motivation.
    * Ziele der Dokumentation und Abgrenzung.
    * Schwerpunkte der Dokumentation.
    * Übersicht zu den einzelnen Kapiteln, sodass der rote Faden zu den Zielvorstellungen deutlich wird.
* Hauptteil
    * Praktischen oder ggf. wissenschaftlichen Relevanz des Themas
    * Die Begründung für die Struktur und Inhalte der folgenden Kapitel soll vermittelt
    werden.
    * Die Position der Einzelkapitel im Rahmen der Gesamtdarstellung mit deren
    * Bedeutung für den Themenschwerpunkt ist zu verdeutlichen.

    * Jedes Kapitel beginnt mit einer Übersicht zu den zu erwartenden Beiträgen. Fakten, Begründungen, Implikationen und Alternativenvergleiche sind im Vorrang zu Bewertungen und Stellungnahmen zu behandeln.
    * Diskussion der Literatur
    * Die beabsichtigten weiteren Recherchen, theoretischen Analysen, zu erstellende Konzepte und Implementierungen sind zu skizzieren. Eine Einordnung und Gewichtung des im Vortrag behandelten Themas in die voraussichtliche Masterarbeit ist anzustreben.
