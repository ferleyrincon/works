# Diccionario de variables

Generado en 2026 a partir de `iat/models.py` y `survey/models.py` (etiquetas tal como las vieron los participantes, recortadas a 110 caracteres). Variables estándar de oTree (`participant.*`, `session.*`) no se listan.

## App `iat`, modelo `Player` (una fila por participante y bloque; 7 filas por participante)

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `identificador` | Char | Recuerde que su código de participante está compuesto por las iniciales de su primer nombre y apellido segu... |  |
| `treatment` | Integer | Por favor seleccione el grupo al que fue asignado | 0=C; 1=T |

## App `iat`, modelo `Trial` (una fila por ensayo; 110 por participante)

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `block` | Integer | block |  |
| `trial` | Integer | trial |  |
| `stimulus` | Char | stimulus |  |
| `stimulus_class` | Char | stimulus class |  |
| `stimulus_level` | Char | stimulus level |  |
| `response_key` | Char | response key |  |
| `response_correct` | Boolean | response correct | True=Si; False=No |
| `response_time_ms` | Integer | response time ms |  |

## App `survey`, modelo `Player` (una fila por participante), en el orden de `page_sequence`

### Página `beliefs`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `p_science1` | PositiveInteger | Requieren muchos años de estudio. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_science2` | PositiveInteger | Son monótonos. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_science3` | PositiveInteger | Son solitarios. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_science4` | PositiveInteger | Pagan salarios altos. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_science5` | PositiveInteger | Hacen difícil el balance familia-trabajo. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_gender1` | PositiveInteger | Los hombres nacen con habilidades diferentes a las mujeres. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_gender2` | PositiveInteger | Las mujeres son mejores en matemáticas que los hombres. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_gender3` | PositiveInteger | Los hombres son mejores científicos que las mujeres. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_gender4` | PositiveInteger | Las mujeres son mejores programadoras que los hombres. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_gender5` | PositiveInteger | Las ingenierías son profesiones para hombres. | 1=1; 2=2; 3=3; 4=4; 5=5 |

### Página `efficacy`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `p_math1` | PositiveInteger | Me gusta la ciencia en general. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_math2` | PositiveInteger | Me siento perdida o perdido cuando trato de resolver un problema de matemáticas. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_math3` | PositiveInteger | menudo me preocupa que tendré dificultades en la clase de matemáticas. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_math4` | PositiveInteger | Si me esfuerzo lo suficiente, puedo hacerlo bien en las materias de ciencias. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_jobsci1` | PositiveInteger | Algunos trabajos en ciencia son interesantes. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_jobsci2` | PositiveInteger | Podría verme trabajando en un trabajo relacionado con la ciencia más adelante en la vida. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_jobsci3` | PositiveInteger | Las perspectivas de carrera y de ingresos juegan un papel importante en mi elección de estudio. | 1=1; 2=2; 3=3; 4=4; 5=5 |

### Página `group`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `i_mat` | Integer | Matemáticas | 0=Hombres; 1=Mujeres |
| `i_spa` | Integer | Lectura Crítica | 0=Hombres; 1=Mujeres |
| `i_sci` | Integer | Ciencias Naturales | 0=Hombres; 1=Mujeres |
| `i_soc` | Integer | Sociales y Ciudadanas | 0=Hombres; 1=Mujeres |

### Página `saber11`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `prueba_20000` | Char | prueba 20000 |  |
| `prueba_15000` | Char | prueba 15000 |  |
| `prueba_10000` | Char | prueba 10000 |  |
| `prueba_5000` | Char | prueba 5000 |  |
| `puntaje_20000` | Integer | puntaje 20000 |  |
| `puntaje_15000` | Integer | puntaje 15000 |  |
| `puntaje_10000` | Integer | puntaje 10000 |  |
| `puntaje_5000` | Integer | puntaje 5000 |  |
| `prefer_20000` | Integer | prefer 20000 |  |
| `prefer_15000` | Integer | prefer 15000 |  |
| `prefer_10000` | Integer | prefer 10000 |  |
| `prefer_5000` | Integer | prefer 5000 |  |
| `predic_20000` | Integer | predic 20000 |  |
| `predic_15000` | Integer | predic 15000 |  |
| `predic_10000` | Integer | predic 10000 |  |
| `predic_5000` | Integer | predic 5000 |  |
| `grupo_puntaje_global` | Integer | grupo puntaje global |  |

### Página `explicit`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `e_tec` | Integer | Informática y Tecnología | 0=Hombre; 1=Mujer |
| `e_sci` | Integer | Naturales (Biología, Física y Química) | 0=Hombre; 1=Mujer |
| `e_mat` | Integer | Matemáticas | 0=Hombre; 1=Mujer |
| `e_spa` | Integer | Español | 0=Hombre; 1=Mujer |
| `e_soc` | Integer | Sociales (Geografía, Historia y Democracia) | 0=Hombre; 1=Mujer |
| `e_art` | Integer | Artes | 0=Hombre; 1=Mujer |

### Página `subjects`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `l_mat` | PositiveInteger | Matemáticas | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `l_art` | PositiveInteger | Artes | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `l_soc` | PositiveInteger | Sociales (Geografía, Historia y Democracia) | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `l_spa` | PositiveInteger | Español | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `l_sci` | PositiveInteger | Naturales (Biología, Física y Química) | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `l_tec` | PositiveInteger | Informática y Tecnología | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_sci` | PositiveInteger | Naturales (Biología, Física y Química) | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_tec` | PositiveInteger | Informática y Tecnología | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_spa` | PositiveInteger | Español | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_soc` | PositiveInteger | Sociales (Geografía, Historia y Democracia) | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_art` | PositiveInteger | Artes | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_mat` | PositiveInteger | Matemáticas | 1=1; 2=2; 3=3; 4=4; 5=5 |

### Página `occupation`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `occupation_1` | Char | occupation 1 |  |
| `time_occupation_1` | Float | time occupation 1 |  |
| `occupation_2` | Char | occupation 2 |  |
| `time_occupation_2` | Float | time occupation 2 |  |
| `occupation_3` | Char | occupation 3 |  |
| `time_occupation_3` | Float | time occupation 3 |  |
| `time_init_occupation` | Float | time init occupation |  |

### Página `occupation2`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `educ_type` | Integer | ¿Para hacer lo que más le gusta es necesaria una carrera? | 1=Técnica; 2=Tecnológica; 3=Profesional; 4=Ninguna |
| `educ_university` | Char | Escriba el nombre de la institución educativa en la que desea estudiar. También puede escribir NO SÉ |  |
| `educ_university2` | Char | ¿Tiene una segunda opción? En caso de que sí, escriba el nombre de la institución educativa donde también l... |  |

### Página `careers`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `career1` | PositiveInteger | Administración, Contaduría Pública, Economía. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career2` | PositiveInteger | Agronomía, Veterinaria, Zootecnia. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career3` | PositiveInteger | Antropología, Psicología, Historia. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career4` | PositiveInteger | Artes Plásticas, Visuales y Artes Afines. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career5` | PositiveInteger | Biología, Física, Química. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career6` | PositiveInteger | Deportes, Educación Física, Recreación. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career7` | PositiveInteger | Derecho, Filosofía, Ciencia Política. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career8` | PositiveInteger | Diseño, Publicidad. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career9` | PositiveInteger | Educación. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career10` | PositiveInteger | Estadística. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career11` | PositiveInteger | Ingeniería de Sistemas, Telemática y Afines. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career12` | PositiveInteger | Ingeniería Electrónica, Telecomunicaciones y Afines. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career13` | PositiveInteger | Ingeniería Mecánica, Industrial, Civil. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career14` | PositiveInteger | Ingeniería Química, Metalúrgica, Petróleos. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career15` | PositiveInteger | Lenguas Modernas. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career16` | PositiveInteger | Licenciaturas. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career17` | PositiveInteger | Literatura. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career18` | PositiveInteger | Matemáticas. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career19` | PositiveInteger | Medicina, Enfermería, Bacteriología. | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `career20` | PositiveInteger | Odontología, Optometría, Instrumentación Quirúrgica. | 1=1; 2=2; 3=3; 4=4; 5=5 |

### Página `education`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `educsup` | Integer | educsup |  |
| `check_slider_educsup` | Integer | check slider educsup |  |

### Página `time`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `p_risk` | PositiveInteger | ¿Qué tan dispuesto (a) está o no está usted a tomar riesgos? | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_time` | PositiveInteger | ¿Qué tan dispuesto está a renunciar a algo que es beneficioso para usted en este momento a fin de obtener m... | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_time2` | PositiveInteger | ¿Qué tan dispuesto está a posponer las tareas, incluso cuando sabe que sería mejor hacerlas de inmediato? | 1=1; 2=2; 3=3; 4=4; 5=5 |

### Página `questions1`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `p_vocational` | Integer | 1. ¿Ha participado antes en alguna actividad de orientación vocacional/profesional? | 1=Sí; 2=No |
| `p_sex` | Integer | 2. ¿Cuál es su sexo? | 0=Hombre; 1=Mujer |
| `p_age` | Integer | 3. ¿Cuántos años cumplidos tiene? |  |
| `p_colombian` | Integer | 4. País de nacimiento: | 1=Colombia; 2=Otro país |
| `p_urban` | Integer | 5. Área de residencia: | 1=Rural; 2=Urbana |
| `p_tech` | Integer | 6. Seleccione la especialidad en la cual actualmente se encuentra | 1=Actividad física y deport; 2=Administración empresaria; 3=Dibujo técnico.; 4=Electricidad y electrónic; 5=Mecánica ... |
| `p_desertion` | Integer | 7. ¿Alguna vez tuvo que suspender sus estudios? | 1=No.; 2=Sí, por dificultades acad; 3=Sí, por dificultades en e; 4=Sí, por enfermedad.; 5=Sí, por falta de interés ; ... |
| `p_years` | Integer | 8. ¿Ha reprobado algún año? | 0=No, no he perdido ningún ; 1=Sí, estudié y no aprobé l; 2=Sí, por dificultades en e; 3=Sí, por enfermedad.; 4=Sí, n... |
| `p_internet` | Integer | 9. ¿En su hogar cuenta con acceso o conexión a internet? | 0=No.; 1=Sí, al menos un teléfono ; 2=Sí, un computador portáti; 3=Sí, un computador de escr |
| `p_lavadora` | Integer | 10. ¿Su hogar cuenta con una máquina lavadora de ropa? | 0=No.; 1=Sí |

### Página `questions2`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `p_care` | Integer | 11. De 1 (nada) a 5 (completamente), ¿qué tanto cree que ayudar en su casa dificulta su proceso de aprendiz... | 1=1; 2=2; 3=3; 4=4; 5=5 |
| `p_family` | Integer | 12. ¿Cuántas personas conforman el hogar donde vive actualmente, incluido usted? | 0-15 |
| `p_siblings` | Integer | 13. ¿Cuántas hermanas y hermanos tiene usted en total? | 0-10 |
| `p_rooms` | Integer | 14. En total, ¿en cuántos cuartos duermen las personas de su hogar? | 0-10 |
| `p_estrato` | Integer | 15.Según el recibo de energía ¿Cuál es el estrato de la vivienda en la que reside con sus padres o núcleo f... | 0-6 |
| `p_pension2` | Integer | 16. ¿Qué están haciendo (hicieron) sus padres para mantenerse económicamente en la vejez? | 1=Aportando en un fondo de ; 2=Aportando en un fondo de ; 3=Ahorrando; 4=Haciendo inversiones; 5=Pagando un seguro po... |
| `edu_father` | Integer | 17. ¿Cuál es el nivel educativo más alto alcanzado por su padre | 1=Ninguno; 2=Primaria; 3=Secundaria (Bachillerato); 4=Técnico o tecnológico; 5=Pregrado (Universitario); 6=Posgrado (... |
| `edu_mother` | Integer | 18. ¿Cuál es el nivel educativo más alto alcanzado por su madre | 1=Ninguno; 2=Primaria; 3=Secundaria (Bachillerato); 4=Técnico o tecnológico; 5=Pregrado (Universitario); 6=Posgrado (... |
| `career_father` | Char | 19.Escriba el nombre de la profesión de su padre |  |
| `career_mother` | Char | 20.Escriba el nombre de la profesión de su madre |  |
| `ocu_mother` | Integer | 22. Ocupación u oficio del madre | 1=Es agricultora, pesquera ; 2=Es dueña de un negocio gr; 3=Es dueña de un negocio pe; 4=Es operaria de máquinas o; 5... |
| `ocu_father` | Integer | 21. Ocupación u oficio del padre | 1=Es agricultor, pesquero o; 2=Es dueño de un negocio gr; 3=Es dueño de un negocio pe; 4=Es operario de máquinas o; 5... |

### Página `thanks`

| variable | tipo | etiqueta | valores |
|---|---|---|---|
| `comments` | Char | Comentario |  |

