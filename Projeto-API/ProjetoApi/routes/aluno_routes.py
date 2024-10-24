from flask import Blueprint
from controllers.aluno_controller import get_alunos, create_aluno, update_aluno, delete_aluno

alunos_bp = Blueprint('alunos', __name__)

alunos_bp.route('/alunos', methods=['GET'])(get_alunos)
alunos_bp.route('/alunos', methods=['POST'])(create_aluno)
alunos_bp.route('/alunos/<int:aluno_id>', methods=['PUT'])(update_aluno)
alunos_bp.route('/alunos/<int:aluno_id>', methods=['DELETE'])(delete_aluno)