@echo off
echo === INICIANDO WORKFLOW KNIME EN MODO BATCH ===
echo.

echo Ruta actual: %cd%
echo Intentando ejecutar KNIME desde:
echo "C:\Users\garci\AppData\Local\Programs\KNIME\knime.exe"
echo.

"C:\Users\garci\AppData\Local\Programs\KNIME\knime.exe" -nosplash -consoleLog -application org.knime.product.KNIME_BATCH_APPLICATION -workflowDir="C:\Users\garci\OneDrive\Documentos\knime workflows\bd ETL\bd ETL" > knime_log.txt 2>&1


echo.
echo === EJECUCIÓN TERMINADA ===
pause
