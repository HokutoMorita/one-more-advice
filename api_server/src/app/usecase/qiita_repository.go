package usecase

import (
	"one_more_advice_api/src/app/domain"
)

type QiitaRepository interface {
	SelectQiitaItems() []domain.QiitaItem
}
