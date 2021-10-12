package controllers

import (
	"fmt"
	"one_more_advice_api/src/domain"
	"one_more_advice_api/src/interfaces/database"
	"one_more_advice_api/src/usecase"

	"github.com/labstack/echo"
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
