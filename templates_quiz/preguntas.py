preguntas_basicas = {
        'pregunta_1': {'enunciado':['¿Cuántos días tiene una semana?'],
        'alternativas': [['8 días.', 0], 
                        ['7 días.', 1], 
                        ['4 días.', 0], 
                        ['31 días.', 0]
                        ]},
        'pregunta_2': {'enunciado':['¿Quién escribió "Romeo y Julieta"?'],
        'alternativas': [['Alexander Beck.', 0], 
                        ['William Shakespeare.', 1], 
                        ['Napoleon Bonaparte.', 0], 
                        ['Juan Arango', 0]
                        ]},       
        'pregunta_3': {'enunciado':['¿Qué gas necesitamos para respirar?'],
        'alternativas': [['Comida.', 0], 
                        ['Oxígeno.', 1], 
                        ['Dormir', 0], 
                        ['Hidrógeno', 0]
                        ]}
    }

preguntas_intermedias = {
        'pregunta_1': {'enunciado':['¿Qué famoso científico desarrolló la teoría de la relatividad?'],
        'alternativas': [['Albert Einstein.', 1],
                        ['Nikola Tesla.', 0],
                        ['Frank Oppenheimer.', 0],
                        ['Isaac Newton', 0]
                        ]},
        'pregunta_2': {'enunciado':['¿Cuál es la fuerza que mantiene a los objetos en movimiento en el espacio y evita que se detengan?'],
        'alternativas': [['La inercia.', 1],
                        ['La gravitatoria.', 0],
                        ['La fricción.', 0], 
                        ['La velocidad', 0]
                        ]},
        'pregunta_3': {'enunciado':['¿Cuál es el país que se extiende a lo largo de dos continentes, Europa y Asia?'],
        'alternativas': [['Turquía.', 1],
                        ['Georgia.', 0],
                        ['Armenia.', 0], 
                        ['Italia', 0]
                        ]}
    }

preguntas_avanzadas = {
        'pregunta_1': {'enunciado':['¿Quién fue el líder de los derechos civiles en Estados Unidos que pronunció su famoso discurso "I Have a Dream" en 1963?'],
        'alternativas': [['Malcolm X', 0], 
                        ['Martin Luther King Jr.', 1], 
                        ['Abraham Lincoln', 0], 
                        ['Rosa Parks', 0]
                        ]},
        'pregunta_2': {'enunciado':['¿Qué evento se considera que desencadenó la Primera Guerra Mundial?'],
        'alternativas': [['La formación de alianzas militares entre países europeos.', 0], 
                        ['El asesinato del archiduque Francisco Fernando de Habsburgo.', 1], 
                        ['Conflictos Territoriales en los Balcanes.', 0], 
                        ['El desarrollo de nuevas tecnologías militares.', 0]
                        ]},  
        'pregunta_3': {'enunciado':['¿Qué faraón egipcio es conocido por haber intentado que su imperio pasase del politeísmo al monoteísmo a través del culto al dios Atón?'],
        'alternativas': [['Amenhotep III', 0], 
                        ['Akenatón', 1], 
                        ['Ramsés II', 0], 
                        ['Tutankamón', 0]
                        ]}
    }

pool_preguntas = {'basicas': preguntas_basicas,
                    'intermedias': preguntas_intermedias,
                    'avanzadas': preguntas_avanzadas}
