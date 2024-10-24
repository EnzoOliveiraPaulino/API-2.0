from flask import Blueprint
from controllers.professor_controller import get_professores, create_professor, get_professor

professores_bp = Blueprint('professores', __name__)


# Professores routes
professores_bp.route('/professores', methods=['GET'])(get_professores)
professores_bp.route('/professores', methods=['POST'])(create_professor)
professores_bp.route('/professores/<int:professor_id>', methods=['GET'])(get_professor)