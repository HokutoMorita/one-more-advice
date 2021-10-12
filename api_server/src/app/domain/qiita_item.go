package domain

import (
	"time"
)

type QiitaItem struct {
	ItemId string `json:"item_id" gorm:"primary_key"`
	Text string `json:"text"`
	Coediting bool `json:"coediting"`
	CommentsCount int `json:"comments_count"`
	CreatedAt time.Time `json:"created_at"`
	LikesCount int `json:"likes_count"`
	Private bool `json:"private"`
	ReactionsCount int `json:"reactions_count"`
	Title string `json:"title"`
	UpdatedAt time.Time `json:"updated_at"`
	Url string `json:"url"`
	PageViewsCount int `json:"page_views_count"`
	UserId string `json:"user_id"`
}
