# Implementación de Redes Neuronales en Microcontroladores

La integración de redes neuronales en microcontroladores representa un avance significativo en el ámbito de los sistemas embebidos, permitiendo dotar a dispositivos de bajo consumo y recursos limitados con capacidades de inteligencia artificial.

## Proceso de Implementación

El proceso de implementación de una red neuronal en un microcontrolador abarca varias etapas fundamentales:

1. **Adquisición de Datos**: Recolección de datos relevantes que servirán para entrenar la red neuronal.
2. **Entrenamiento de la Red**: Utilización de herramientas y plataformas para entrenar la red neuronal con los datos recopilados.
3. **Implementación en el Microcontrolador**: Traducción del modelo entrenado a un formato compatible con el microcontrolador seleccionado.
4. **Validación**: Pruebas exhaustivas para asegurar que la red neuronal funciona correctamente en el entorno embebido.

Este flujo de trabajo garantiza que la red neuronal se adapte adecuadamente a las restricciones y características del microcontrolador.

## Generación y Entrenamiento de la Red Neuronal

Para facilitar la creación y entrenamiento de redes neuronales destinadas a microcontroladores, se puede utilizar el siguiente Jupyter Notebook:

- [generacion_red_neuronal.ipynb](https://github.com/dgomezh92/generador_redneuronal_embebida/blob/main/creacion_red_neuronal_y_entrenamiento/generacion_red_neuronal.ipynb)

Este notebook guía al usuario a través de los pasos necesarios para diseñar, entrenar y preparar una red neuronal que pueda ser implementada en un entorno embebido.

## Motor de Inferencia en C++

Una vez entrenada la red neuronal, es esencial contar con un motor de inferencia eficiente que permita su ejecución en el microcontrolador.

El repositorio [vehiculo_con_red_neuronal](https://github.com/dgomezh92/vehiculo_con_red_neuronal) proporciona un motor de inferencia en C++ diseñado para ejecutar redes neuronales feedforward.

### Características Principales del Motor de Inferencia

- **Configurabilidad**: Permite definir el número de capas y neuronas por capa, adaptándose a las necesidades específicas del proyecto.
- **Funciones de Activación**: Incluye funciones comunes como RELU, SIGMOID, TANH y LINEAR.
- **Asignación de Pesos**: Facilita la inicialización manual de pesos, lo que es útil cuando se entrena el modelo en herramientas externas como TensorFlow o PyTorch.

Este motor de inferencia está diseñado para ser sencillo y eficiente, permitiendo su uso tanto por personal técnico como por desarrolladores que buscan integrar inteligencia artificial en sistemas embebidos.

La implementación de redes neuronales en microcontroladores abre nuevas posibilidades en el desarrollo de dispositivos inteligentes, optimizando procesos y mejorando la interacción con el entorno.
