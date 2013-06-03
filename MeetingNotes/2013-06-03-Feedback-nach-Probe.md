* Around slide 70
    * Mention that the pipeline pattern is very easily implementable in Google Go.
        * "Handshake" zwischzen den Patterns
    * Mention other patterns that are easily implementable in Google Go
        * Zeigen dass es auch noch was anderes kann

* "Die Kurve kriegen" zurück zur Platform
    * Google-Go Threadpool abgebildet auf zwei CPUs
    * platform erwähnen, wie stages auf cores abgebildet usw
    * was macht jetzt ein thread, und wie ordnet man es den cpus zu
    * scheduling verhalten in go (runtime)
    * Vielleicht noch irgendwie erwähnen, dass man da drin auch SIMD benutzen kann (also in Go)

* Bessere Differenzierung (#2)
    * Pipeline Pattern (mehr Software)
    * SIMD (mehr Hardware) (µP)
    * Wie kann ich das am besten klar machen?

* Brücke Thread <-> CPU (#19)
    * ggf Assembly Line erklärung eindampfen

* Slide #40
    * Symbolisieren dass das Register noch größer ist als 3 elemente

* Wie kompiliert man das jetzt? am beispiel von gcc mit options und so

* Next Milestones (Slide #72)
    * Erprobungsbeispiel
        * Implementation of current Java subsystem in either language
        * Possibly using Pipeline pattern and SIMD

* Quellen aus Kurzausarbeitung
