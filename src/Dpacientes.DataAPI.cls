Class Dpacientes.DataAPI
{

ClassMethod GetAllPatients() As %String
{
    Set result = ##class(%DynamicArray).%New()
    &sql(DECLARE C CURSOR FOR SELECT id, name, age, coverage FROM SQLUser.Patient)
    &sql(OPEN C)
    While (SQLCODE=0) {
        &sql(FETCH C INTO :id, :name, :age, :coverage)
        If (SQLCODE=0) {
            Set obj = ##class(%DynamicObject).%New()
            Do obj.%Set("id", id)
            Do obj.%Set("name", name)
            Do obj.%Set("age", age)
            Do obj.%Set("coverage", coverage)
            Do result.%Push(obj)
        }
    }
    &sql(CLOSE C)
    Return result.%ToJSON()
}

}
