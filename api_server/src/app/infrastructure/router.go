package infrastructure

import (
	"fmt"
	controllers "one_more_advice_api/src/app/interfaces/api"
	"net/http"
	"github.com/labstack/echo"
)

func Init() {
	// Echo instance
	e := echo.New()
	qiitaController := controllers.NewQiitaController(NewSqlHandler())
	fmt.Println("ルーティングを開始しました")

	e.GET("/qiita_items", func(c echo.Context) error {
		fmt.Println("Qiita記事データ取得リクエストを受け付けました")
		qiitaItems := qiitaController.GetQiitaItems()
		c.Bind(&qiitaItems)
		return c.JSON(http.StatusOK, qiitaItems)
	})

	// Start server
	e.Logger.Fatal(e.Start(":1323"))
}
