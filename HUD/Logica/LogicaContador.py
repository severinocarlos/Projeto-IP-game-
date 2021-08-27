from HUD.Dados import DadosContador as DC
from HUD.Dados import DadosPokemonsColetados as DPC
from HUD.Dados import DadosRocket as DR
from Janela.Dados import DadosTelaFinal as DTF
import RodarJogo as RJ

def Contador(TempoInicio,TempoAposExecucao):
    DC.TempoCorrido += TempoAposExecucao-TempoInicio
    DC.TempoParaContador += TempoAposExecucao-TempoInicio
    if DC.TempoParaContador>=1:
        DC.TempoRestante-=1
        DC.TempoParaContador-=1
    DC.Texto = str(DC.TempoRestante)
    if DC.TempoRestante<10:
        DC.MenorQue10 = True
    if DC.TempoRestante <=0:
        if DR.NumeroRocket>= DPC.NumeroPokemons:
            DTF.Derrota = True
        else:
            DTF.Sucesso = True
        DTF.TelaFinal = True
        RJ.StartGame = False