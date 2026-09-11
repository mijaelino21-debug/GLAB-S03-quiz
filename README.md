Laboratorio 03: Creación de Modelos en Django — App Quiz

Estudiante: Mijael Lino Curso: Desarrollo de Aplicaciones Empresariales

Descripción

Aplicación Django que gestiona exámenes con preguntas de opción múltiple. Se implementaron los modelos Exam, Question y Choice, sus formularios y formset, vistas para listar y crear contenido, y su registro en el panel de administración.

Estructura del proyecto

<img width="1198" height="459" alt="image" src="https://github.com/user-attachments/assets/80ce02df-0d21-41b7-9cf2-7dfe99772185" />

Migraciones

Se generaron 4 migraciones a lo largo del laboratorio:

0001_initial.py: creación del modelo Exam.
0002_question_choice.py: creación de los modelos Question y Choice.
0003_alter_choice_options_alter_exam_options_and_more.py: clases Meta (ordering, verbose_name).
0004_question_score.py: campo nuevo score agregado a Question.

Vistas

Se implementaron 3 vistas: exam_list (listado), exam_detail (detalle con preguntas y opciones), y question_create (alta de pregunta con validación de que exactamente una opción sea correcta antes de guardar).

Durante las pruebas se encontró y corrigió un error NoReverseMatch: el redirect() de question_create apuntaba a 'exam_detail' sin el namespace, y al tener las urls registradas con namespace='quiz' debía ser 'quiz:exam_detail'.

Admin y datos de prueba

Los tres modelos se registraron en el admin (ExamAdmin, QuestionAdmin con ChoiceInline, ChoiceAdmin). Se creó un examen de prueba ("Examen de Matemáticas Básicas") con 4 preguntas y 4 opciones cada una.
<img width="1914" height="425" alt="image" src="https://github.com/user-attachments/assets/adbe1b4b-fd64-4c90-a8b4-dbc271b10952" />

<img width="1908" height="790" alt="image" src="https://github.com/user-attachments/assets/2f58c92f-38cc-4d75-bfae-120a32211d08" />

<img width="886" height="378" alt="image" src="https://github.com/user-attachments/assets/82433a7d-47ff-405a-bec0-7f44948c111a" />

<img width="886" height="400" alt="image" src="https://github.com/user-attachments/assets/65eed76c-b9fc-4f95-a6f7-7ec1a9badde5" />



