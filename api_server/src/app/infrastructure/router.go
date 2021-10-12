package infrastructure

import (
	controllers "one_more_advice_api/src/app/interfaces/api"
	"net/http"
	"github.com/labstack/echo"
)

func Init() {
	// Echo instance
	e := echo.New()
	qiitaController := controllers.NewQiitaController(NewSqlHandler())

	e.GET("/qiita_items", func(c echo.Context) error {
		qiitaItems := qiitaController.GetQiitaItems()
		c.Bind(&qiitaItems)
		return c.JSON(http.StatusOK, qiitaItems)
	})
}
