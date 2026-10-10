profissoes = {
    "cardiologista":"Médico especialista em corações",
    "professor":"Profissional em ensinar",
    "desenvolvedor de sistemas":"Desenvolvedor de Softwares",
    "motoboy":"Entregador de comida",
}
resultado = input("Digite a profissão que você quer conhecer: ").strip().lower()

while resultado not in profissoes:
    print("Escolha uma profissão válida")
    resultado = input("Digite a profissão que você quer conhecer: ").strip().lower()
   
print(profissoes[resultado])