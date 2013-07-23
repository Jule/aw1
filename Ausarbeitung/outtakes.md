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





<!--\clearpage-->
# blub
<!--\todoin{Komprimierte Darstellung der wesentlichen Inhalte}-->

<!--\todoin{Ausblick (wie geht es weiter?)}-->

<!--\todoin{Schwarz: Software Engineering for Embedded Systems: Methods, Practical Techniques, and Applications (Expert Guide)? \url{http://goo.gl/vM360}
}-->

<!--\todoin{Hier im Ausblick erwähnen, dass Performance-Vergleiche anhand eigener Anwendungen folgen, bezogen auf SIMD stuff aber auch Go auf embedded (vs. C/C++)}-->

<!--\todoin{Literatur Recherche zu
Concurrency und aktuellen MPSOC.
(Multiprocessor System-on-Chip: Hardware Design and Tool Integration)
Paralleliserung von Laserscanner und Kamera Datenstromverarbeitung unter Linux mit GO im Wettstreit mit C-Threads-pur.
}-->

<!--\todoin{Mention that \citep{Herlihy2012} will be used as an additional "fundation work", since it was revised in 2012 and thus is newer, but was not available to the author until now.}-->

<!--\todoin{Ausblick: As a result, the impact of Go's garbage collector on application performance will have to be closely evaluated (also scheduling stuff)}-->

<!--\todoin{Mention that the NEON Alchemy Lab stuff must be confirmed.}-->

<!--\todoin{Schwarz: The Art of Multiprocessor Programming sollten wir auch auf dem Zettel haben, da hier eine neue Auflage vorliegt. \url{http://goo.gl/TZU73}
}-->

<!--\todoin{short essay outlook: In the course of my master seminar, these hypotheses will be evaluated by extracting performance critical elements from the mentioned FAUST application and implementing them in Go and C, using state of the art dataflow parallelization algorithms. These implementations will then be compared to their original (non-parallelized) counterparts, in terms of performance, ease of implementation and implementation complexity.}-->







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
