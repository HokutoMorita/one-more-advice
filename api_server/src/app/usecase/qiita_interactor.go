package usecase

import (
	"one_more_advice_api/src/app/domain"
)

type QiitaInteractor struct {
	QiitaRepository QiitaRepository
}

func (interactor *QiitaInteractor) GetQiitaItems() []domain.QiitaItem {
	return interactor.QiitaRepository.SelectQiitaItems()
}
