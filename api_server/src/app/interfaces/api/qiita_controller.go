package controllers

import (
	"one_more_advice_api/src/app/domain"
	"one_more_advice_api/src/app/interfaces/database"
	"one_more_advice_api/src/app/usecase"
)

type QiitaController struct {
	Interactor usecase.QiitaInteractor
}

func NewQiitaController(sqlHandler database.SqlHandler) *QiitaController {
	return &QiitaController{
		Interactor: usecase.QiitaInteractor{
			QiitaRepository: &database.QiitaRepository{
				SqlHandler: sqlHandler,
			},
		},
	}
}

func (controller *QiitaController) GetQiitaItems() []domain.QiitaItem {
	return controller.Interactor.GetQiitaItems()
}
