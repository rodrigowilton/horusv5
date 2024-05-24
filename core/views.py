import requests
import webbrowser
from django.shortcuts import render
from django.http import HttpResponse

from core.forms import CondominioForm
from core.models import (Apartamentos, Abastecimentos, AberturasPortas, AcessosApp, AgendamentoHorarios,
Agendamentos, Areas, AreasParalelas, Atendimentos, Atividades, AtividadesMateriaisProdutos, AtividadesOrdemdeservicos,
AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, CamFacials,
CardsElevadors, CentraisJfls, Chamadas, ChavesVirtuais, ChecklistObras, Codigos, ComercialEtapas, ComercialLeadEtapas,
ComercialLeadProcessos, ComercialLeads, ComercialProcessos, ComercialProspeccao, Comodatos,CondominioEquipamentos,
Condominios, CondominiosFeriados, CondominiosFuncionarios, CondominiosFuncionariosDispositivosRoles, ConfigFacials,
ConfigOs, ContatoEmergencias, ControlesAcessos, Convidados, Criticidades, Departamentos, Dispositivos, DispositivosAcessos,
DispositivosCards, DispositivosCardsTipos, DispositivosEventos, DispositivosMarcas,DispositivosModelos, DispositivosRegistros,
DispositivosRoles, DispositivosRolesDispositivosAcessos, DispositivosTipos, DjangoAdminLog, DjangoContentType,DjangoMigrations,
DjangoSession, Documentos, ElevadorChamados, Empresas, EmpresasServicos, EmpresasServicosEmpresas, Encomendas,
EntregadoresNormas, EstadosEquipamentos, Eventos, EventosTratados,Faturamentos, FaturamentosMateriais,FaturamentosOrcamentos,
Feriados, Ferramentas, Fotos, Funcionarios, GruposEventos, GruposZonas, HistoricoCondominios, HistoricoPessoas, Imagemcameras,
Informativos, Internets, ItensCadastrados, ItensOrcamentos, ItensVistorias, LiberacoesAcessos, LiberacoesChaves, MateriaisAtividades,
MateriaisGrupos, MateriaisMarcas, MateriaisObras, MateriaisProdutos, MateriaisUnidades, MudancasNormas, Notificacoes, Obras,
ObrasChecklistObras, Ocorrencias, Orcamentos, OrcamentosMateriais, OrcamentosPessoas, Ordemdeservicos, OrdemdeservicosMateriaisProdutos,
Parcelas, Patrimonios, Pedagios, PermissaoAcessos, PermissaoAcessosDispositivosRoles, Pessoas, PessoasDispositivosRoles, Pets,
Pgms, PlantaoOcorrencias, PlantaoOperacionals, Portas, PrestadoresAcessos, PrestadoresNormas, Projetos, Qths, QthsTarefas,
QthsTarefasQths, Questionarios, Racas, Recados, ReconhecidoFacials, ReservasNormas, Roles, Sindicos, Subramais, SubtiposOcorrencias,
SubtiposOcorrenciasOcorrencias, SubtiposTiposAbastecimentos, Suporteunidades, Tarefas, TatticaFuncionarios, TatticaTelefones,
TatticaVeiculos, TiposAbastecimentos, TiposAcessos, TiposClassificacaos, TiposCondominiosFuncionarios,TiposControlesAcessos,
TiposElevadorChamados, TiposEncomendas, TiposEquipamentos, TiposEventosTratados, TiposFotos, TiposFuncionarios, TiposOcorrencias,
TiposOcorrenciasOcorrencias, TiposPagamentos, TiposPatrimonios, TiposPedagios, TiposPessoas, TiposProjetos, TiposRacas,
TiposSindicos, TiposTarefas, TiposVeiculos, TiposZonas, Tips, TipsTatticaFuncionarios, Unidades, Users, Vagas,Veiculos,
Vistorias, VistoriasItensVistorias, Zonas)


def condominio(request):
    return render(request, 'condominio.html')
def unidades(request):
    unidades_list = Unidades.objects.all()
    nomes_unidades = [unidade.nome_unidade for unidade in unidades_list]
    return render(request, 'unidades.html', {'unidades': unidades_list})


def internets(request):
    internet_list = Internets.objects.all()
    nome_internet = [internet.nome_internet for internet in internet_list]
    return render(request, 'internets.html', {'internets': internet_list})


def cameras_view(request):
    url = "http://192.168.2.254:8081/#!/login?token=eyJ1c2VyTmFtZSI6ImFkbWluIn0.Wuf-5rC-MmXEaujDUJNCJ_ZZ17GkXC7ljQajDcvOenM&continue={\"path\":\"live\",\"search\":{\"layout\":\"%7B1E813852-98D4-4926-8DD1-1D6F3D15C823%7D\"}}"

    try:
        # Faça a requisição GET
        response = requests.get(url, timeout=10)  # Timeout de 10 segundos

        # Verifique se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Obtenha o conteúdo da resposta
            conteudo = response.text
            # Abrir a resposta no navegador
            webbrowser.open_new(url)
        else:
            conteudo = f"Erro na requisição: {response.status_code}"

    except requests.exceptions.RequestException as e:
        conteudo = f"Ocorreu um erro: {e}"

    #return render(request, 'cameras/cameras.html', {'conteudo': conteudo})
    return render(request, 'index.html', {'conteudo': conteudo})


def index(request):
    condominios = Condominios.objects.all()
    return render(request, 'index.html', {'condominios': condominios})


def agenda(request):
    return render(request, 'menu_agenda.html')


def config(request):
    return render(request, 'menu_adm.html')


def contatos(request):
    return render(request, 'menu_contatos.html')


def informacoes(request):
    return render(request, 'menu_informacoes.html')


def ocorrencias(request):
    return render(request, 'menu_ocorrencias.html')


def servicos(request):
    return render(request, 'menu_servicos.html')


def solicitacoes(request):
    return render(request, 'menu_solicitacoes.html')


def telefones(request):
    return render(request, 'menu_telefones.html')

