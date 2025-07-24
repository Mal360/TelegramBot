__all__ = ('router',)

from aiogram import Router

from .base_commands import router as base_commands_router
from .one_c_commands import router as one_c_commands_router
from .reclamations_commands import router as reclamations_router
from .knowledge_base_commands import router as knowledge_base_router
from .equipment_maintenance_commands import router as equipment_maintenance_router
from .about_company_commands import router as about_company_router
from .nesting_check_commands import router as nesting_check_router
from .technical_support_commands import router as technical_support_router

router = Router(name=__name__)

router.include_routers(base_commands_router,
                       one_c_commands_router,
                       reclamations_router,
                       knowledge_base_router,
                       equipment_maintenance_router,
                       about_company_router,
                       nesting_check_router,
                       technical_support_router)
