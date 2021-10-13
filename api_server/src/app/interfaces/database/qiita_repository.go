package database

import (
	"one_more_advice_api/src/app/domain"
)

type QiitaRepository struct {
	SqlHandler
}

func (db *QiitaRepository) SelectQiitaItems() []domain.QiitaItem {
	qiitaItems := []domain.QiitaItem{}
	db.FindAll(&qiitaItems)
	return qiitaItems
}
