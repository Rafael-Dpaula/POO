from personagem import Personagem
from missao import MissaoColeta, MissaoCombate, MissaoExploracao
from item import Item
from tipo_item import TipoItem
from status import Status


def ler_int(mensagem: int):
    try:
        valor = int(input(mensagem).strip())
        return valor
    except ValueError:
        print("Entrada inválida. Digite um inteiro.")


def ler_float(mensagem: str):
    try:
        valor = float(input(mensagem).strip())
        return valor
    except ValueError:
        print("Entrada inválida. Digite um número.")


def ler_str(mensagem: str):
        valor = input(mensagem).strip()
        if valor == "":
            print("Entrada não pode ser vazia.")
        else:
            return valor


def escolher_personagem(personagens: list[Personagem]) -> Personagem:
    while True:
        print("Escolha o personagem:")
        for i, p in enumerate(personagens, start=1):
            print(f"{i} - {p.nome} (Nível {p.nivel} | Vida {p.vida})")
        idx = ler_int("Opção: ")
        return personagens[idx - 1]


def listar_missoes(missoes: list) -> None:
    if not missoes:
        print("Nenhuma missão.")
        return
    for i, m in enumerate(missoes, start=1):
        status = getattr(m, "status", None)
        status_txt = status.value if status is not None else ""
        print(f"{i} - {m.nome} | [{status_txt}]")
        print(f"    {m.descricao}")


def listar_inventario(personagem: Personagem) -> None:
    if not personagem.inventario:
        print("Inventário vazio.")
        return
    for i, item in enumerate(personagem.inventario, start=1):
        print(f"{i} - {item.nome} | Tipo: {item.tipo.value} | Efeito: {item.valorEfeito} | {item.descricao}")


def buscar_item_por_indice(inventario: list[Item], mensagem: str) -> Item | None:
    if not inventario:
        print("Inventário vazio.")
        return None
    listar_inventario(Personagem("tmp"))  # não usada; só para manter função simples
    # acima não está correto; vamos listar diretamente
    return None


def menu_principal():
    personagens: list[Personagem] = [Personagem("Zen"), Personagem("Mark")]

    # Catálogo simples de itens/missões (para facilitar testagem)
    missoes_catalogo: list = [
        MissaoCombate(
            nome="Extermínio Sombrio",
            descricao="Derrote criaturas corrompidas na floresta",
            recompensa=50,
            inimigo="Corrompido",
            inimigos_a_derrotar=5,
        ),
        MissaoCombate(
            nome="Limpar a dungeon norte",
            descricao="Derrote todos as criaturas presentes no 1º andar da dungeon norte",
            recompensa=50,
            inimigo="Goblins",
            inimigos_a_derrotar=18,
        ),
        MissaoExploracao(
            nome="Explorador de Arcadia",
            descricao="Explore a região esquecida ao norte",
            recompensa=30,
            local="Ruínas Antigas",
            distancia=12.5,
        ),
        MissaoColeta(
            nome="Coleta de Ervas",
            descricao="Colete ervas medicinais raras",
            recompensa=15,
            item_necessario="Erva Lunar",
            quantidade_item=10,
        ),
    ]

    itens_catalogo: list[Item] = [
        Item(
            "Espada de Ferro Rúnico",
            "Uma lâmina antiga com inscrições mágicas desgastadas.",
            15,
            TipoItem.ARMA,
        ),
        Item("Arco Silvestre", "Feito de madeira élfica, leve e preciso.", 12, TipoItem.ARMA),
        Item(
            "Armadura de Couro Endurecido",
            "Proteção básica usada por aventureiros iniciantes.",
            8,
            TipoItem.VESTIMENTA,
        ),
        Item("Capa Sombria", "Dificulta ser detectado em áreas escuras.", 5, TipoItem.VESTIMENTA),
        Item("Poção de Vida", "Restaura pontos de vida ao ser consumida.", 20, TipoItem.UTILITARIO),
        Item(
            "Bomba de Fumaça",
            "Permite escapar rapidamente de combates.",
            0,
            TipoItem.UTILITARIO,
        ),
    ]

    personagem_atual = escolher_personagem(personagens)

    while True:
        print("\n==============  MENU  ==============")
        print(f"Personagem atual: {personagem_atual.nome} | Nível {personagem_atual.nivel} | Vida {personagem_atual.vida}")
        print("0 - Trocar personagem")
        print("1 - Mostrar personagem")
        print("2 - Mostrar inventário do personagem")
        print("3 - Mostrar missões do personagem")
        print("4 - Adicionar item ao inventário (criando manualmente ou pelo catálogo)")
        print("5 - Remover item do inventário")
        print("6 - Equipar itens (arma/vestimenta/utilitário) do inventário")
        print("7 - Criar missão e adicionar ao personagem")
        print("8 - Lista de missões disponíveis no catálogo / e adicionar ao personagem")
        print("9 - Concluir missão (informar valor coletado/derrotado/percorrido)")
        print("10 - Criar item e adicionar ao inventário")
        print("11 - Mostrar catálogo de itens e missões")
        print("12 - Sair")

        opcao = ler_int("Escolha: ", minimo=0, maximo=12)

        if opcao == 12:
            break

        if opcao == 0:
            personagem_atual = escolher_personagem(personagens)
            continue

        if opcao == 1:
            personagem_atual.exibir_dados()
            continue

        if opcao == 2:
            listar_inventario(personagem_atual)
            continue

        if opcao == 3:
            listar_missoes(personagem_atual.missoes)
            continue

        if opcao == 11:
            print("\n--- Catálogo de Itens ---")
            for i, it in enumerate(itens_catalogo, start=1):
                print(f"{i} - {it.nome} | Tipo: {it.tipo.value} | Efeito: {it.valorEfeito}")
            print("\n--- Catálogo de Missões ---")
            for i, m in enumerate(missoes_catalogo, start=1):
                status_txt = m.status.value if hasattr(m, "status") else ""
                print(f"{i} - {m.nome} | Tipo: {m.__class__.__name__} | [Status: {status_txt}]")
            continue

        if opcao == 4:
            print("\nAdicionar item ao inventário")
            print("1 - Criar manualmente")
            print("2 - Escolher do catálogo")
            sub = ler_int("Escolha: ", minimo=1, maximo=2)

            if sub == 2:
                for i, it in enumerate(itens_catalogo, start=1):
                    print(f"{i} - {it.nome} ({it.tipo.value})")
                idx = ler_int("Item: ", minimo=1, maximo=len(itens_catalogo))
                item_escolhido = itens_catalogo[idx - 1]
                personagem_atual.add_Item(item_escolhido)
            else:
                nome = ler_str("Nome do item: ")
                desc = ler_str("Descrição: ")
                valorEfeito = ler_float("Valor do efeito (numérico): ")
                print("Tipos disponíveis:")
                for t in TipoItem:
                    print(f"- {t.name} ({t.value})")
                tipo_str = ler_str("Tipo do item (ex: ARMA/VESTIMENTA/UTILITARIO): ").upper()
                tipo = TipoItem[tipo_str] if tipo_str in TipoItem.__members__ else None
                if tipo is None:
                    print("Tipo inválido.")
                    continue
menu_principal()