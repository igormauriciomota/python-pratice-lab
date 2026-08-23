def resumir_nota(notas):
    if not notas:
        raise ValueError("Informe ao menos uma nota.")


    if any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("As notas devem ficar entre 0 e 10.")


    return {
        "quantidade": len(notas),
        "media": sum(notas) / len(notas),
        "menor": min(notas),
        "maior": max(notas)
    }    


notas = []
for texto in ["7.5", "8", "9.2"]:
    notas.append(float(texto))

print(resumir_nota(notas))
