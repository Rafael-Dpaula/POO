# Menu interativo simples (teste) para o RPG

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.personagem import Personagem
from models.item import Item
from models.tipo_item import TipoItem
from models.missao import MissaoColeta, MissaoCombate, MissaoExploracao


def _print_header(txt: str):
    print("\n" + "=" * 10 + f" {txt} " + "=" * 10)


def _read_int(msg: str, minimo=None, maximo=None):
    while True:
        raw = input(msg).strip()
        try:
            v = int(raw)
        except ValueError:
            print("Digite um número válido.")
            continue
        if minimo is not None and v < minimo:
            print(f"Valor deve ser >= {minimo}")
            continue
        if maximo is not None and v > maximo:
            print(f"Valor deve ser <= {maximo}")
            continue
        return v


def _read_float(msg: str, minimo=None, maximo=None):
    while True:
        raw = input(msg).strip()
        try:
            v = float(raw)
        except ValueError:
            print("Digite um número válido.")
            continue
        if minimo is not None and v < minimo:
            print(f"Valor deve ser >= {minimo}")
            continue
        if maximo is not None and v > maximo:
            print(f"Valor deve ser <= {maximo}")
            continue
        return v


def _read_str(msg: str):
    while True:
        s = input(msg).strip()
        if s == "":
            print("Entrada não pode ser vazia.")
            continue
        return s


def _find_item_by_name(itens, nome: str):
    for it in itens:
        if it.nome == nome:
            return it
    return None


def _find_missao_by_name(missoes, nome: str):
    for m in missoes:
        if m.nome == nome:
            return m
    return None


def main():
    personagens = [Personagem("Zen"), Personagem("Mark")]
    personagem = personagens[0]

    itens_disponiveis = [
        Item("Espada de Ferro Rúnico", "Uma lâmina antiga com inscrições mágicas desgastadas.", 15, TipoItem.ARMA),
        Item("Arco Silvestre", "Feito de madeira élfica, leve e preciso.", 12, TipoItem.ARMA),
        Item("Armadura de Couro Endurecido", "Proteção básica usada por aventureiros iniciantes.", 8, TipoItem.VESTIMENTA),
        Item("Capa Sombria", "Dificulta ser detectado em áreas escuras.", 5, TipoItem.VESTIMENTA),
        Item("Poção de Vida", "Restaura pontos de vida ao ser consumida.", 20, TipoItem.UTILITARIO),
        Item("Bomba de Fumaça", "Permite escapar rapidamente de combates.", 0, TipoItem.UTILITARIO),
    ]

    missoes_disponiveis = [
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

    while True:
        _print_header("MENU PRINCIPAL")
        print(f"Personagem ativo: {personagem.nome}")
        print("1) Personagens")
        print("2) Itens")
        print("3) Equipar")
        print("4) Missões")
        print("5) Sair")

        secao = _read_int("Escolha (1-5): ", 1, 5)

        # ====== PERSONAGENS ======
        if secao == 1:
            while True:
                _print_header("PERSONAGENS")
                print("Personagens disponíveis:")
                for i, p in enumerate(personagens):
                    ativo = "(ATIVO)" if p.nome == personagem.nome else ""
                    print(f"  {i}) {p.nome} {ativo}")

                print("\n1) Trocar personagem")
                print("2) Ver dados do personagem")
                print("3) Mostrar inventário")
                print("4) Listar missões do personagem")
                print("5) Criar novo personagem")
                print("6) Voltar")

                a = _read_int("Escolha (1-6): ", 1, 6)

                if a == 1:
                    idx = _read_int("Índice: ", 0, len(personagens) - 1)
                    personagem = personagens[idx]
                elif a == 2:
                    personagem.exibir_dados()
                elif a == 3:
                    personagem.mostrar_Inventario()
                elif a == 4:
                    print("\nMissoes:")
                    for m in personagem.missoes:
                        print(f"  - {m.nome} | status={m.status.value}")
                    if not personagem.missoes:
                        print("  (nenhuma)")
                elif a == 5:
                    nome = _read_str("Nome do personagem: ")
                    p = Personagem(nome)
                    personagens.append(p)
                    personagem = p
                    print(f"Personagem '{personagem.nome}' criado e ativo.")
                else:
                    break

        # ====== ITENS ======
        elif secao == 2:
            while True:
                _print_header("ITENS")
                print("Itens disponíveis (para adicionar no inventário):")
                for i, it in enumerate(itens_disponiveis):
                    print(f"  {i}) {it.nome} | tipo={it.tipo.value} | efeito={it.valorEfeito}")

                print("\n1) Adicionar item ao inventário")
                print("2) Remover item do inventário")
                print("3) Mostrar inventário do personagem")
                print("4) Criar novo item")
                print("5) Voltar")

                b = _read_int("Escolha (1-5): ", 1, 5)

                if b == 1:
                    idx = _read_int("Índice do item: ", 0, len(itens_disponiveis) - 1)
                    personagem.add_Item(itens_disponiveis[idx])
                elif b == 2:
                    nome = _read_str("Nome exato do item a remover: ")
                    # como o Personagem só remove por referência encontrada na lista disponível no menu,
                    # buscamos na lista de itens disponíveis.
                    item = _find_item_by_name(itens_disponiveis, nome)
                    if item is None:
                        print("Item não existe na lista de itens disponíveis deste menu.")
                    else:
                        personagem.remove_Item(item)
                elif b == 3:
                    personagem.mostrar_Inventario()
                elif b == 4:
                    print("\n=== CRIAR ITEM ===")
                    nome = _read_str("Nome do item: ")
                    descricao = _read_str("Descrição: ")
                    valorEfeito = _read_float("ValorEfeito (número): ")
                    print("Tipos: 1) ARMA  2) VESTIMENTA  3) UTILITÁRIO")
                    t = _read_int("Escolha (1-3): ", 1, 3)
                    tipo = TipoItem.ARMA if t == 1 else (TipoItem.VESTIMENTA if t == 2 else TipoItem.UTILITARIO)
                    novo = Item(nome, descricao, valorEfeito, tipo)
                    itens_disponiveis.append(novo)
                    print(f"Item '{novo.nome}' criado e adicionado na lista disponível.")
                else:
                    break

        # ====== EQUIPAR ======
        elif secao == 3:
            while True:
                _print_header("EQUIPAR")
                personagem.mostrar_Inventario()
                print("\nEscolha os itens para equipar (precisa estar no inventário).")

                def _filtrar_por_tipo(tipo):
                    return [it for it in personagem.inventario if it.tipo == tipo]

                armas = _filtrar_por_tipo(TipoItem.ARMA)
                vests = _filtrar_por_tipo(TipoItem.VESTIMENTA)
                utils = _filtrar_por_tipo(TipoItem.UTILITARIO)

                print("\nArmas disponíveis no inventário:")
                if not armas:
                    print("  (nenhuma)")
                else:
                    for i, it in enumerate(armas):
                        print(f"  {i}) {it.nome} | efeito={it.valorEfeito}")

                print("\nVestimentas disponíveis no inventário:")
                if not vests:
                    print("  (nenhuma)")
                else:
                    for i, it in enumerate(vests):
                        print(f"  {i}) {it.nome} | efeito={it.valorEfeito}")

                print("\nUtilitários disponíveis no inventário:")
                if not utils:
                    print("  (nenhuma)")
                else:
                    for i, it in enumerate(utils):
                        print(f"  {i}) {it.nome} | efeito={it.valorEfeito}")

                print("\n1) Equipar (arma + vestimenta + utilitário)")
                print("2) Ver dados do personagem")
                print("3) Voltar")

                c = _read_int("Escolha (1-3): ", 1, 3)
                if c == 1:
                    if not armas or not vests or not utils:
                        print("Equipamento incompleto: equipe um item de cada tipo (arma/vest/util).")
                        continue
                    ia = _read_int("Índice da arma: ", 0, len(armas) - 1)
                    iv = _read_int("Índice da vestimenta: ", 0, len(vests) - 1)
                    iu = _read_int("Índice do utilitário: ", 0, len(utils) - 1)
                    personagem.equiparItens(armas[ia], vests[iv], utils[iu])
                elif c == 2:
                    personagem.exibir_dados()
                else:
                    break

        # ====== MISSÕES ======
        elif secao == 4:
            while True:
                _print_header("MISSÕES")
                print("Missoes disponíveis (para adicionar ao personagem):")
                for i, m in enumerate(missoes_disponiveis):
                    print(f"  {i}) {m.nome} | status={m.status.value} | recompensa={m.recompensa}")

                print("\nMissoes do personagem:")
                if not personagem.missoes:
                    print("  (nenhuma)")
                else:
                    for m in personagem.missoes:
                        print(f"  - {m.nome} | status={m.status.value}")

                print("\n1) Adicionar missão ao personagem")
                print("2) Concluir missão")
                print("3) Criar nova missão")
                print("4) Voltar")

                d = _read_int("Escolha (1-4): ", 1, 4)

                if d == 1:
                    idx = _read_int("Índice da missão: ", 0, len(missoes_disponiveis) - 1)
                    missao = missoes_disponiveis[idx]
                    resultado = personagem.add_missao(missao)
                    if isinstance(resultado, str):
                        print(resultado)
                elif d == 2:
                    nome_missao = _read_str("Nome exato da missão a concluir: ")
                    missao = _find_missao_by_name(personagem.missoes, nome_missao)
                    if missao is None:
                        print("Missão não está na lista do personagem.")
                        continue
                    raw = input("Valor de progresso (0..quantidade ou distância): ").strip()
                    try:
                        valor = float(raw)
                    except ValueError:
                        print("Valor inválido.")
                        continue
                    print(personagem.concluir_missao(missao, valor))
                elif d == 3:
                    print("\n=== CRIAR MISSÃO ===")
                    print("Tipos: 1) Combate  2) Coleta  3) Exploracao")
                    t = _read_int("Escolha (1-3): ", 1, 3)
                    nome = _read_str("Nome da missão: ")
                    descricao = _read_str("Descrição: ")
                    recompensa = _read_int("Recompensa (0..50): ", 0, 50)

                    if t == 1:
                        inimigo = _read_str("Inimigo: ")
                        qtd = _read_int("Inimigos a derrotar (>=1): ", 1)
                        nova = MissaoCombate(
                            nome=nome,
                            descricao=descricao,
                            recompensa=recompensa,
                            inimigo=inimigo,
                            inimigos_a_derrotar=qtd,
                        )
                    elif t == 2:
                        item_necessario = _read_str("Nome do item necessário (deve existir no mundo do jogador): ")
                        qtd_item = _read_int("Quantidade de item necessário (>=1): ", 1)
                        nova = MissaoColeta(
                            nome=nome,
                            descricao=descricao,
                            recompensa=recompensa,
                            item_necessario=item_necessario,
                            quantidade_item=qtd_item,
                        )
                    else:
                        local = _read_str("Local/Região: ")
                        distancia = _read_float("Distância (>=0): ", 0.0001)
                        nova = MissaoExploracao(
                            nome=nome,
                            descricao=descricao,
                            recompensa=recompensa,
                            local=local,
                            distancia=distancia,
                        )

                    missoes_disponiveis.append(nova)
                    print(f"Missão '{nova.nome}' criada e adicionada na lista disponível.")
                else:
                    break

        else:
            _print_header("SAINDO")
            break


if __name__ == "__main__":
    main()

