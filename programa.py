def asignar_memoria(blockSize, processSize):
    blockSize.sort()  # Ordenar bloques de memoria en orden ascendente
    asignado = [-1] * len(processSize)  # Lista para rastrear la asignación de memoria

    for i in range(len(processSize)):
        for j in range(len(blockSize)):
            if blockSize[j] >= processSize[i]:
                asignado[i] = j  # Asignar el índice del bloque adecuado
                blockSize[j] -= processSize[i]  # Restar el tamaño del proceso del bloque correspondiente

                if (blockSize[j]== 0) or (processSize[i]-blockSize[j]== 0):
                    blockSize.pop(j)  # Eliminar el bloque si su tamaño se reduce a cero
                break

    # Mostrar el estado final de la lista de bloques libres
    print("Estado final de la lista de bloques libres:")
    print(blockSize)

    # Mostrar la asignación de memoria para cada proceso
    print("Asignación de memoria para cada proceso:")
    for i in range(len(processSize)):
        if asignado[i] != -1:
            print("Proceso", i, "asignado al bloque", asignado[i]+1)
        else:
            print("Proceso", i, "no se pudo asignar suficiente memoria")

# Ejemplo de uso
blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]
blockSize.sort()
print("Valor inicial de los bloques ordenados:\n{}".format(blockSize))
asignar_memoria(blockSize, processSize)
