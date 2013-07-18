# Intro

As modern embedded applications evolve, their performance requirements increase. Due to the limitations of embedded platforms, such as constraints in power consumption and heat dissipation, these increased performance requirements cannot be met by increasing processor clock rates.

Consequently, modern embedded platforms increasingly feature more than a single processing core, thus offering high-performance computing capabilities, while preservering low-power consumption constraints <!--\citep{Wang2013}-->.


# Techniques

that operate on multiple data simultaneously (i.e. in parallel), namely "Single instruction, multiple data" (SIMD) and "Multiple instruction, multiple data" (MIMD). This categorization is often called Flynn's Taxonomy, which also describes


## MIMD

include multiprocessor systems, and as such are almost universally available in todays desktop computers, and increasingly available on embedded platforms. Furthermore, many modern multi-core microprocessors feature SIMD subsystems, such as Intel's SSE extensions, and

# Stuff that provides parallelism

* E.g. on a relatively high level, one can use threads
* But there are also things like GPUs, SIMD etc

