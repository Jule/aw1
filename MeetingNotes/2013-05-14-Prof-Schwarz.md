* Grundaufbau:
    1. Struktur (Plattform/HW/SW)
    2. Methodik (Algorithmen)
    2. Instrument (Google Go)

**Fokus auf den Dingen die bisher unscharf sind!**

---

* Konkretisierung der Plattform
* Grobstruktur Hardware/Software
    * Laserscanner (ist: Java/Android)
        * Details? Datendurchsatz, etc?
    * Spurführung (ist: FPGA/C-Module)
        * Videology [24B752XA](http://www.videologyinc.com/media/products/data%20sheet/24B752XA/PDS-24B752XA.pdf)
        * 60FPS 752x480px 27MHz
    * Momentan recht "buntes" Konglomerat von Dingen
    * Aussicht: Soll unifiziert werden, wie? Schafft Ordnung auf der Plattform

* Methodik Parallelisierung
    * Algorithmen "rauspicken". Genaue Evaluation in diesem Zeitfenster nicht möglich, deshalb "π*Daumen".
        * Entsprechende Algorithmen erläutern (1 < n < 4)
    * Ein wenig darauf eingehen was für SIMD Dinge ARM NEON so kann (auch an Prof. Schwarz)
    * Grobe Analyse des bestehenden Problems
        * Was für Daten habe ich?
        * Wie muss ich sie modifizieren?
        * Wo ist parallelisierung überhaupt möglich (exploitable concurrency)?

* Instrument:
    * Google Go
    * Wie gut ist die Performance auf Embedded (vergleich mit C).
        * Datendurchsatz-Test?
    * In wiefern ist der Code tatsächlich einfacher/besser implementierbar als in C?
        * Zeigen von Code-Schnipseln!
