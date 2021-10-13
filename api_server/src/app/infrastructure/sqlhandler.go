package infrastructure

import (
	"os"
	"fmt"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"one_more_advice_api/src/app/interfaces/database"
)

type SqlHandler struct {
	db *gorm.DB
}

func NewSqlHandler() database.SqlHandler {
	mysqlPassword := os.Getenv("MYSQL_PASSWORD")
	mysqlDatabase := os.Getenv("MYSQL_DATABASE")
	mysqlHost := os.Getenv("MYSQL_HOST")
	mysqlUser := os.Getenv("MYSQL_USER")
	mysqlPort := os.Getenv("MYSQL_PORT")
	// dsn := "root:one_more_advice@tcp(127.0.0.1:4307)/one_more_advice_prog?collation=utf8mb4_unicode_ci&parseTime=true"
	dsn := mysqlUser + ":" + mysqlPassword + "@tcp(" + mysqlHost + ":" + mysqlPort + ")/" + mysqlDatabase + "?collation=utf8mb4_unicode_ci&parseTime=true"
	
	db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		fmt.Println("DBへの接続に失敗しました")
		fmt.Println(err)
		panic(err.Error)
	}
	sqlHandler := new(SqlHandler)
	sqlHandler.db = db
	return sqlHandler
}

func (handler *SqlHandler) Create(obj interface{}) {
	handler.db.Create(obj)
}

func (handler *SqlHandler) FindAll(obj interface{}) {
	handler.db.Find(obj)
}

func (handler *SqlHandler) FindById(obj interface{}, id int) {
	handler.db.First(obj, id)
}

func (handler *SqlHandler) DeleteById(obj interface{}, id string) {
	handler.db.Delete(obj, id)
}

func (handler *SqlHandler) UpdateAll(obj interface{}) {
	handler.db.Save(obj)
}
