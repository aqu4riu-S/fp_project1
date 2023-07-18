# 99187 bruno miguel vaz e campos

def eh_tabuleiro(tab):
    # universal -> booleano
    '''recebe um argumento de qualquer tipo e devolve True se este
    corresponder a um tabuleiro; False, caso contrario'''
    if isinstance(tab, tuple) and len(tab) == 3:
        for el in tab:
            if not isinstance(el, tuple) or not len(el) == 3:
                return False
            for val in el:
                if val not in (-1, 0, 1) or type(val) != int:
                    return False
        return True   
    else:
        return False
    

def eh_posicao(pos):
    # universal -> booleano
    '''recebe um argumento de qualquer tipo e devolve True se este corresponde
    a uma posicao e False caso contrario'''
    return type(pos) == int and 1 <= pos <= 9
    

def obter_coluna(tab, inteiro):
    # tabuleiro x inteiro -> vetor
    '''recebe um tabuleiro e um inteiro com valor de 1 a 3 que representa o
    numero da coluna, e devolve um vetor com os valores dessa coluna'''
    if eh_tabuleiro(tab) and type(inteiro) == int and 1 <= inteiro <= 3:
        index = inteiro - 1
        return (tab[0][index], tab[1][index], tab[2][index])     
    else:
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    
    
def obter_linha(tab, inteiro):
    # tabuleiro x inteiro -> vetor
    '''recebe um tabuleiro e um inteiro com valor de 1 a 3 que representa o
    numero da linha e devolve um vetor com os valores dessa linha'''
    if eh_tabuleiro(tab) and type(inteiro) == int and 1 <= inteiro <= 3:
        return tab[inteiro - 1]      
    else:
        raise ValueError('obter_linha: algum dos argumentos e invalido')    


def obter_diagonal(tab, inteiro):
    # tabuleiro x inteiro -> vetor
    '''recebe um tabuleiro e um inteiro que representa a direcao da diagonal,
    1 para descendente, da esquerda para a direita, 2 para ascendente, da
    esquerda para a direita, e devolve um vetor com os valores dessa diagonal'''
    if eh_tabuleiro(tab) and type(inteiro) == int and \
       inteiro == 1 or inteiro == 2:
        if inteiro == 1:
            return (tab[0][0], tab[1][1], tab[2][2])
        else:
            return (tab[2][0], tab[1][1], tab[0][2])    
    else:
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')    
    
 
def tabuleiro_str(tab):
    # tabuleiro -> cadeia de carateres
    '''recebe um tabuleiro e devolve a cadeia de carateres que o representa'''
    if eh_tabuleiro(tab):
        tab_str = ''
        comp = len(tab)
        for i in range(comp):
            for ii in range(comp):
                if tab[i][ii] == 1:
                    tab_str += ' X'
                elif tab[i][ii] == -1:
                    tab_str += ' O'
                else:
                    tab_str += '  '
                if ii != 2:
                    tab_str += ' |'
            if i != 2:
                tab_str += ' \n-----------\n'
            else:
                tab_str += ' '
        return tab_str            
    else:
        raise ValueError('tabuleiro_str: o argumento e invalido')


def eh_posicao_livre(tab, inteiro):
    # tabuleiro x posicao -> booleano
    '''recebe um tabuleiro e uma posicao e devolve True se essa corresponde
    a uma posicao livre do tabuleiro e Falseca so contrario'''
    if eh_tabuleiro(tab) and eh_posicao(inteiro):
        index = inteiro - 1
        return tab[index // 3][index % 3] == 0
    else:
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')

    
def obter_posicoes_livres(tab):
    # tabuleiro -> vetor
    '''recebe um tabuleiro e devolve o vetor ordenado com todas as posicoes
    livres desse tabuleiro'''
    if eh_tabuleiro(tab):
        pos_livres = ()
        comp = len(tab)
        for i in range(comp):
            for ii in range(comp):
                if tab[i][ii] == 0:
                    pos_livres += ((i * 3 + ii % 3 + 1),)
        return pos_livres
    else:
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
    

#-----------------------------Funcao Auxiliar----------------------------------#
#------------------------da funcao jogador_ganhador----------------------------#

def compara_fila(vetor):
    # vetor -> inteiro
    '''recebe um vetor correspondente a uma fila (linha, coluna ou diagonal) e
    devolve 1 caso se o jogador com o 'X' ganhou, ou -1 se o jogador com o 'O' 
    ganhou'''
    if -1 not in vetor and 0 not in vetor:
        return 1
    elif 1 not in vetor and 0 not in vetor:
        return -1
    
#------------------------------------------------------------------------------#

def jogador_ganhador(tab):
    # tabuleiro -> inteiro
    '''recebe um tabuleiro e devolve um valor inteiro a indicar o jogador que
    ganhou a partida no tabuleiro passado por argumento, sendo o valor 1 se 
    ganhou o jogador que joga com 'X', -1 se ganhou o jogador que joga com 'O' 
    ou 0 se nao ganhou nenhum jogador'''
    if eh_tabuleiro(tab):
        for i in range(1, 4):
            linha = obter_linha(tab, i)
            res = compara_fila(linha)
            if res != None:
                return res
            coluna = obter_coluna(tab, i)
            res = compara_fila(coluna)
            if res != None:
                return res            
        for i in range(1,3):
            diagonal = obter_diagonal(tab, i)
            res = compara_fila(diagonal)
            if res != None:
                return res            
        return 0    
    else:
        raise ValueError('jogador_ganhador: o argumento e invalido')



def marcar_posicao(tab, val, pos):
    # tabuleiro x inteiro x inteiro -> tabuleiro 
    '''recebe um tabuleiro, um inteiro identificando um jogador (1 para o
    jogador 'X' ou -1 para o jogador 'O', e uma posicao livre, e devolve um novo
    tabuleiro modificado com uma nova marca do jogador nessa posicao'''
    if eh_tabuleiro(tab) and (val == 1 or val == -1) and type(val) == int \
       and eh_posicao(pos) and eh_posicao_livre(tab, pos): 
        index = pos - 1
        linha = index // 3
        col = index % 3
        tab_modif = (tab[:linha] + ((tab[linha][:col] + (val,) \
                                     + tab[linha][col+1:]),) + tab[linha+1:])
        return tab_modif
    else:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')



def escolher_posicao_manual(tab):
    # tabuleiro -> posicao
    '''realiza a leitura de uma posicao introduzida manualmente por um
    jogador e devolve esta posicao escolhida. a funcao pede ao utilizador para
    introduzir uma posicao livre'''
    if eh_tabuleiro(tab):
        pos = eval(input('Turno do jogador. Escolha uma posicao livre: '))
        if eh_posicao(pos) and eh_posicao_livre(tab, pos):
            return pos
        else:
            raise ValueError('escolher_posicao_manual: ' + \
                             'a posicao introduzida e invalida')
    else:
        raise ValueError('escolher_posicao_manual: o argumento e invalido')

 
#------------------------------Funcoes Auxiliares------------------------------#
#-----------------------da funcao escolher_posicao_auto------------------------#

def soma_fila(vetor):
    # vetor -> int
    '''recebe um vetor respondente a uma fila (linha, coluna ou diagonal) e 
    devolve a soma dos elementos dessa fila'''
    soma = 0
    for el in vetor:
        soma += el
    return soma


def escolhe_menor(vetor):
    # vetor -> inteiro
    '''recebe um vetor de inteiros de devolve o menor deles'''
    menor_num = 9
    for el in vetor:
        if el < menor_num:
            menor_num = el
    return menor_num



def pos_vitoria(vetor, inteiro):
    # vetor x inteiro -> inteiro
    '''recebe um vetor correspondente a uma fila (linha, coluna ou diagonal) 
    e um inteiro associado a marca de jogo de um jogador (1 para jogador que 
    joga com o 'X', -1 para jogador que joga com o 'O') e devolve o index 
    do vetor relativo a posicao de jogo que permite fazer a jogada vencedora 
    ou bloquear a jogada vencedora do oponente'''
    if soma_fila(vetor) == 2 * inteiro:
        # ver qual das posicoes esta vazia e retornar o seu index em caso
        # afirmativo; i eh o index do vetor
        for i in range(3):
            if vetor[i] == 0:
                return i
        

def estrat_1_2(tab, inteiro):
    # tab x inteiro -> inteiro
    '''recebe um tabuleiro de jogo e um inteiro referente ao valor associado
    a marca de jogo de um dado jogador e devolve um inteiro relativo a posicao
    (1 a 9) que permite fazer jogada vencedora ou bloquear jogada vencedora do
    oponente'''
    for i in range(1, 4):
    # i eh o numero da fila
        index_fila = pos_vitoria(obter_linha(tab, i), inteiro)
        if index_fila != None:
            return (i - 1) * 3 + index_fila % 3 + 1
        
        index_fila = pos_vitoria(obter_coluna(tab, i), inteiro)
        if index_fila != None:
            return i + 3 * index_fila
        
    for i in range(1, 3):
        index_fila = pos_vitoria(obter_diagonal(tab, i), inteiro)
        if index_fila != None:
            if i == 1:
                return i + index_fila * 4
            else:
                return 7 - 2 * index_fila  


def estrat_6(tab, inteiro):
    # tabuleiro x inteiro -> inteiro
    '''recebe um tabuleiro e devolve um inteiro relativo a posicao que respeita
    as condicoes da estrategia 6'''
    
    diagonal_1 = obter_diagonal(tab, 1)
    diagonal_2 = obter_diagonal(tab, 2)
    
    if diagonal_1[2] == -inteiro and diagonal_1[0] == 0:
        return 1
    elif diagonal_2[0] == -inteiro and diagonal_2[2] == 0:
        return 3
    elif diagonal_2[2] == -inteiro and diagonal_2[0] == 0:
        return 7            
    elif diagonal_1[0] == -inteiro and diagonal_1[2] == 0:
        return 9    


def estrat_7_8(tab):
    # tabuleiro -> inteiro
    '''recebe um tabuleiro e devolve um inteiro correspondente a menor posicao
    de jogo que respeita as condicoes das estrategias 7 e 8'''
    for num in (1, 3, 7, 9, 2, 4, 6, 8):
        if num in obter_posicoes_livres(tab):
            return num    


def intersecao(vetor1, vetor2, tab):
    # tuplo x tuplo -> inteiro
    '''recebe dois vetores (relativos a linha, coluna ou diagonal), e devolve
    um inteiro relativo a intersecao desses dois vetores'''
    for pos in vetor1:
        if pos in vetor2:
            if eh_posicao_livre(tab, pos):
                return pos         
            
        
def hipoteses_inters(vetor1, vetor2, comp1, comp2, intersecoes, tab):
    # tuplo x tuplo x inteiro x inteiro x tuplo -> tuplo
    '''recebe dois vetores (relativos a linha, coluna ou diagonal), dois 
    inteiros (relativos ao comprimento desses dois vetores), um vetor
    (que guarda todas as posicoes de intersecao de filas) e um tabuleiro, 
    e devolve esse vetor de intersecoes atualizado com a intersecao dos dois 
    vetores passados como argumentos'''
    for i in range(comp1):
        for ii in range(comp2):
            res_inters = intersecao(vetor1[i], vetor2[ii], tab)
            if res_inters != None: 
                intersecoes = intersecoes + (res_inters,)
    return intersecoes



def estrat_3_4(tab, inteiro):
    # tabuleiro x inteiro -> vetor
    '''recebe um tabuleiro e um inteiro referente ao valor associado a marca 
    de jogo do computador e devolve um tuplo com todas as posicoes de
    intersecoes livres'''
    
    tuplo_linhas = ()
    tuplo_colunas = ()
    tuplo_diagonais = ()
    # obter as filas a considerar
    for i in range(1, 4):
        linha = obter_linha(tab, i)
        if soma_fila(linha) == inteiro and 0 in linha:
            # tuplo de posicoes correspondente a essa linha 
            tuplo_linhas = tuplo_linhas + \
                (((i - 1) * 3 + 1, (i - 1) * 3 + 2, (i - 1) * 3 + 3),)
        coluna = obter_coluna(tab, i)
        if soma_fila(coluna) == inteiro and 0 in coluna:
            # tuplo de posicoes correspondente a essa coluna 
            tuplo_colunas = tuplo_colunas + \
                ((i, i + 3, i + 6),)
    for ii in range(1, 3):
        diagonal = obter_diagonal(tab, ii)
        if soma_fila(diagonal) == inteiro and 0 in diagonal:
            # tuplo de posicoes correspondente a essa diagonal 
            if ii == 1:
                tuplo_diagonais = tuplo_diagonais + ((1, 5, 9),)
            else:
                tuplo_diagonais = tuplo_diagonais + ((7, 5, 3),)                           
            
          
    comp_diagonais = len(tuplo_diagonais)
    comp_linhas = len(tuplo_linhas)
    comp_colunas = len(tuplo_colunas)
    intersecoes = ()

    if comp_diagonais > 0:
        
        if comp_linhas > 0:
            intersecoes = hipoteses_inters(tuplo_diagonais,\
            tuplo_linhas, comp_diagonais, comp_linhas, intersecoes, tab)
           
        if comp_colunas > 0:
            intersecoes = hipoteses_inters(tuplo_diagonais,\
        tuplo_colunas, comp_diagonais, comp_colunas, intersecoes, tab)
           
            
    if comp_linhas > 0 and comp_colunas > 0:
        intersecoes = hipoteses_inters(tuplo_linhas,\
            tuplo_colunas, comp_linhas, comp_colunas, intersecoes, tab)

    return intersecoes   


def verifica_dois_em_linha(tab, inteiro):
    # tabuleiro x inteiro -> vetor
    '''recebe um tabuleiro e um inteiro identificando o computador 
    (1 se joga com 'X' ou -1 se joga com 'O') e devolve um tuplo com todas as
    posicoes que fariam um dois em linha'''
    dois_em_linha = ()
    # loop para averiguar se ha dois em linha nas linhas e/ou colunas do 
    # tabuleiro
    for i in range(1, 4):
        linha = obter_linha(tab, i)
        if soma_fila(linha) == inteiro and -inteiro not in linha:
            for ii in range(3):
                if linha[ii] != inteiro:
                    # calculo da posicao (1 a 9) que permite dois em linha 
                    # da linha
                    dois_em_linha += ((i-1) * 3 + ii % 3 + 1,)                                
        coluna = obter_coluna(tab, i)
        if soma_fila(coluna) == inteiro and -inteiro not in linha:
            for ii in range(3):
                if coluna[ii] != inteiro:
                    # calculo da posicao (1 a 9) que permite dois em linha 
                    # da coluna
                    dois_em_linha += (i + 3 * ii,)
    # loop para averiguar se ha dois em linha nas diagonais do tabuleiro
    for i in range(1, 3):
        diagonal = obter_diagonal(tab, i)
        if soma_fila(diagonal) == inteiro and -inteiro not in diagonal:
            for ii in range(3):
                if diagonal[ii] != inteiro:
                    # calculo da posicao (1 a 9) que permite dois em linha 
                    # das diagonais
                    if i == 1:
                        dois_em_linha += (i + 4 * ii,)
                    else:
                        dois_em_linha += (7 - 2 * ii,)
    return dois_em_linha


#------------------------------------------------------------------------------#


def escolher_posicao_auto(tab, inteiro, cad):
    # tabuleiro x inteiro x cadeia de carateres -> posicao
    '''recebe um tabuleiro, um inteiro identificando um jogador (1 para o
    jogador 'X' ou -1 para o jogador 'O'), e uma cadeia de carateres
    correspondente a estrategia, e devolve a posicao escolhida automaticamente
    de acordo com a estrategia selecionada'''
    if eh_tabuleiro(tab) and (inteiro == 1 or inteiro == -1) \
       and type(inteiro) == int and \
       (cad == 'basico' or cad == 'normal' or cad == 'perfeito'):
        
        #------- Modo Basico--------#
        if cad == 'basico':
            
            #------- Estrategia 5--------#
            if eh_posicao_livre(tab, 5):
                return 5
            
            #------- Estrategias 7 e 8--------#
            posicao = estrat_7_8(tab)
            if posicao != None:
                return posicao
            
            
        #------- Modo Normal--------#
        elif cad == 'normal':
            
            #------- Estrategia 1--------#
            posicao = estrat_1_2(tab, inteiro)
            if  posicao != None:
                return posicao
            
            #------- Estrategia 2--------#
            posicao = estrat_1_2(tab, -inteiro)
            if posicao != None:
                return posicao            
            
            #------- Estrategia 5--------#
            if eh_posicao_livre(tab, 5):
                return 5
            
            #------- Estrategia 6--------#
            posicao = estrat_6(tab, inteiro) 
            if posicao != None:
                return posicao
            
            #------- Estrategias 7 e 8-------#
            posicao = estrat_7_8(tab)
            if posicao != None:

                return posicao
            
            
            
        #------- Modo Perfeito--------#    
        else:
            
            #------- Estrategia 1--------#
            posicao = estrat_1_2(tab, inteiro)
            if  posicao != None:
                return posicao
            
            #------- Estrategia 2--------#
            posicao = estrat_1_2(tab, -inteiro)
            
            if posicao != None:
                return posicao  
            
            #------- Estrategia 3--------#
            
            # tuplo com as posicoes de intersecao livres do computador
            intersecoes = estrat_3_4(tab, inteiro)
            if len(intersecoes) != 0:
                # retorna a menor posicao de entre as posicoes de inters livres
                return escolhe_menor(intersecoes)
               
            #------- Estrategia 4-------#
            
            # tuplo com posicoes de intersecao livres do jogador
            intersecoes = estrat_3_4(tab, -inteiro)
            comp_intersecoes = len(intersecoes)
            if comp_intersecoes != 0:
                # se existir apenas uma bifurcacao possivel, computador essa
                # bifurcacao do jogador
                if comp_intersecoes == 1:
                    return intersecoes[0]
                # senao, procura todos os dois em linha possiveis do computador
                else:
                    dois_em_linha = verifica_dois_em_linha(tab, inteiro)
                    # testar se uma dada posicao de dois em linha provocaria
                    # uma bifurcacao quando o oponente defendesse
                    jogadas_pc = ()
                    for el in dois_em_linha:
                        # devolve um tabuleiro apos marcacao com uma posicao
                        # do dois em linha
                        tab_suposicao = marcar_posicao(tab, inteiro, el)
                        # devolve a posicao que o jogador escolheria para 
                        # defender marcacao anterior do computador
                        pos_defesa_jog = estrat_1_2(tab_suposicao, inteiro)
                        # se pos defesa do jogador nao resultar numa bifurcacao
                        if pos_defesa_jog not in intersecoes:
                            jogadas_pc = jogadas_pc + (el,)
                    # retorna a menor posicao de entre as possiveis jogadas        
                    return escolhe_menor(jogadas_pc)
                
            #------- Estrategia 5--------#
            if eh_posicao_livre(tab, 5):
                return 5   
            
            #------- Estrategia 6--------#
            posicao = estrat_6(tab, inteiro) 
            if posicao != None:
                return posicao           
            
            #------- Estrategias 7 e 8--------#
            posicao = estrat_7_8(tab)
            if posicao != None:
                return posicao                                           
    else:
        raise ValueError('escolher_posicao_auto: ' + \
                         'algum dos argumentos e invalido')


#----------------------------Funcao Principal----------------------------------#


def jogo_do_galo(humano, estrategia):
    # cadeia de carateres x cadeia de carateres -> cadeia de carateres
    '''recebe duas cadeias de carateres e devolve o identificaor do jogador
    ganhador ('X' ou 'O'); em caso de empate, devolve a cadeia de carateres
    'EMPATE'. o primeiro argumento corresponde a marca ('X' ou 'O') que o
    jogador humano  deseja utilizar e o segundo argumento seleciona a
    estrategia de jogo utilizada pela maquina'''
    if (humano == 'X' or humano == 'O') and \
       (estrategia == 'basico' or estrategia == 'normal'\
        or estrategia == 'perfeito'):
        tab = (0, 0, 0), (0, 0, 0), (0, 0, 0)
        res = 0
        num_jogadas = 9        
        print('Bem-vindo ao JOGO DO GALO.')
        print("O jogador joga com '" + humano + "'.")    
        turno_jog = True
        if humano != 'X':
            turno_jog = False            
        em_jogo = 1
        
        while res == 0 and num_jogadas > 0:             
            if turno_jog:
                tab = marcar_posicao(tab, em_jogo, escolher_posicao_manual(tab))  
                turno_jog = False 
            else:                
                print('Turno do computador (' + estrategia + '):')
                tab = marcar_posicao(tab, em_jogo, escolher_posicao_auto(tab, em_jogo, estrategia))
                turno_jog = True 
                
            em_jogo = em_jogo * -1
            print(tabuleiro_str(tab))
            # testa se ja existe vencedor
            res = jogador_ganhador(tab)
            num_jogadas -= 1      
                
        if res == 1:
            return 'X'
        elif res == -1:
            return 'O'
        else:
            return 'EMPATE'
    else:
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')