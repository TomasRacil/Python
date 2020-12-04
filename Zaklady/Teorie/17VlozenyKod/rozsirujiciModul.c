#include <Python.h>

//Objekt pro obsluhu vyjímek
static PyObject * exmodError;

static PyObject * exmod_say_something(PyObject* self, PyObject *args){
	const char* msg;
	int sts=0;
	
	//Očekáváme, že obdržíme alespoň jeden argument při volání modulu.
	if(!PyArg_ParseTuple(args,"s",&msg)){
		return NULL; //Vrátí chybu pokud nenalezne argument
	}
	//Ověříme že předaná informace je v pořádku
	if(strcmp(msg,"toto_je_chyba"==0)){
		//pokud chyba pak vyvoláme vyjímku pomocí objektu vyjímky exmodError
		PyErr_SetString(exmodError, "Toto je testovací funkce pro obsluhu chyb předaných v argumentu");
		return NULL; //předáme chybu volajícímu (Python skriptu)
	}else{
		//Pokud nebyla nalezen chyba
		prinntf("Toto je zpráva z C modulu \n a tvoje zpráva je: %s\n",msg);
		sts=21; //vrátíme 0; úspěch
	}
	return Py_BuildValue("i",sts);
}

static PyObject * exmod_add(PyObject* self, PyObject *args){
	double a,b;
	double sts=0;

	//Očekáváme, že obdržíme alespoň jeden argument při volání modulu.
	if(!PyArg_ParseTuple(args,"dd",&a,&b)){
		return NULL; //Vrátí chybu pokud nenalezne argument
	}
	
	sts = a+b;
	printf("Toto je zpráva z C modulu \n a soucet %f a %f je %f",a,b,sts);
	return Py_BuildValue("d",sts);
}

static PyMethodDef exmod_methods[]={
	//"Jmeno v pythonu",	Jmeno v C,		reprezentace argumentů, popis
	{"say_something",	exmod_say_something, 	METH_VARARGS, 		"Vytiskne že je z C modulu a zprávu"},
	{"add",			exmod_add,		METH_VARARGS,		"Sečte dvě čísla v C"},
	{NULL,NULL,0,NULL}	/*Sentinel*/
};

PyMODINIT_FUNC_initexmod(void){
	PyObject *m;
	m= Py_InitModule("exmod", exmod_methods);
	if (m==NULL) return;

	exmodError = PyErr_NewException("exmod.error",NULL,NULL); //"exmod.error" objekt chyby pro Python
	Py_INCREF(exmodError);

	PyModule_AddObject(m,"error",exmodError);
}