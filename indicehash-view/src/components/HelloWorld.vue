<template>
  <!-- 
    Colors:
    - P   = #00bcd4   (D)
    - PC  = #6ff9ff   (D)
    - PD  = #0095a8   (l)
    - S   = #ffa726   (l)
    - SC  = #ffd95b   (l)
    - SD  = #c77800   (l)
   -->
  <v-container>
    <v-alert v-model="notFound" transition="slide-y-transition" type="warning">Palavra Não Encontrada</v-alert>
    <v-alert v-model="error" transition="slide-y-transition" type="error">Vish...</v-alert>
    <div v-if="isInit">
      <v-spacer></v-spacer>
      <v-card color="#00bcd4" dark outlined>
        <v-card-title>TESTE</v-card-title>

        <v-divider class="mx-4"></v-divider>

        <v-row class="ma-4">
          <v-text-field
            label="Pesquisar por..."
            outlined
            clearable
            prepend-inner-icon="mdi-database-search"
            v-model="searchWord"
          >
          </v-text-field>
        </v-row>

        <v-card-actions class="ma-4">
          <v-spacer></v-spacer>
          <v-btn color="#0095a8" @click="pesquisarHash">Pesquisar</v-btn>
        </v-card-actions>
      </v-card>

      <v-card
        class="mt-2"
        v-if="isResponseAvailable"
        color="#00bcd4"
        dark
        outlined
      >
        <v-card-title>Resultado!</v-card-title>
        <v-row class="ma-4">Pagina: {{pag}}</v-row>
        <v-row class="ma-4">Colisão: {{coll}}</v-row>
        <v-row class="ma-4">Overflow: {{overflow}}</v-row>
        <v-row class="ma-4">Acesso: {{access}}</v-row>

      </v-card>

      <v-btn class="mt-2" dark block color="#0095a8" @click="removeHash">REMOVER</v-btn>

      <v-spacer></v-spacer>
    </div>
    <div v-else>
      <v-card color="#00bcd4" dark outlined>
        <v-card-title>Crie seu banco!</v-card-title>
        <v-divider class="mx-4"></v-divider>
        <div class="ma-4">
          <v-row class="ma-4">
            <v-text-field
              class="mr-1"
              label="Tamanho da Pagina"
              outlined
              clearable
              prepend-inner-icon="mdi-database-cog"
              v-model="t_pag"
              type="number"
            >
            </v-text-field>
            <v-text-field
              class="ml-1"
              label="Tamanho do Bucket"
              outlined
              clearable
              prepend-inner-icon="mdi-database-cog"
              v-model="t_bucket"
              type="number"
            >
            </v-text-field>
          </v-row>
          <v-textarea
            class="ma-4"
            label="Seu texto aqui s2"
            outlined
            clearable
            v-model="text"
          ></v-textarea>
          <v-file-input
            dense
            v-model="textFile"
            accept="text/plain"
            placeholder="Ou insira seu arquivo TXT :D"
            prepend-icon="mdi-file"
            @change="loadFile"
          ></v-file-input>
          <v-progress-linear indeterminate rounded color="yellow" :active="fileLoading"></v-progress-linear>
        </div>
        <v-card-actions class="ma-4">
          <v-spacer></v-spacer>
          <v-btn color="#0095a8" :disabled="fileLoading" @click="initHash">Criar</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data() {
    return {
      isInit: false,
      isResponseAvailable: false,

      text: "",
      textFile: null,
      t_bucket: 32,
      t_pag: 16,

      searchWord: "",
      pag: "",
      coll: "",
      overflow: "",
      access: "",

      notFound: false,
      error: false,

      fileLoading: false
    };
  },
  mounted() {
    fetch("http://localhost:3150/hash/initqm")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json)
        this.isInit = json.init;
      });
  },
  methods: {
    loadFile() {
      this.fileLoading = true

      if (this.textFile != null) {
        var reader = new FileReader();

        reader.onload = () => {
          this.text = reader.result;
          this.fileLoading = false;
        };
        reader.readAsText(this.textFile);
      } else {
        this.fileLoading = false; 
      }
    },
    async initHash() {
      console.log(this.t_bucket, this.t_pag)
      console.log(typeof this.t_bucket, typeof this.t_pag)

      await fetch("http://localhost:3150/hash", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: this.text,
          t_bucket: parseInt(this.t_bucket),
          t_pag: parseInt(this.t_pag),
        }),
      });

      fetch("http://localhost:3150/hash/initqm")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json)
        this.isInit = json.init;
      });
    },

    async pesquisarHash() {
      this.isResponseAvailable = false;

      await fetch(`http://localhost:3150/hash/search/${this.searchWord}`)
      .then(response => {
        if (response.status == 404){
          this.notFound = true;
        } else if (response.status != 200) {
          this.error = true;
        } else {
          this.isResponseAvailable = true;
        }

        return response.json();
      })
      .then(json => {
        if (typeof json != undefined) {
          var data = json.data
          console.log(data)

          this.pag = data.pag
          this.coll = data.colission
          this.overflow = data.overflow

          // switch (data.colision) {
          //   case true:
          //     this.coll = "SIM"
          //     break;
          //   case false:
          //     this.coll = "NÃO"
          //     break;
          // }

          this.access = data.access
        }
      })
    },

    async removeHash() {
      await fetch("http://localhost:3150/hash", {
        method: "DELETE"
      });

      await fetch("http://localhost:3150/hash/initqm")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        console.log(json)
        this.isInit = json.init;
      });

      this.searchWord = ""
      this.isResponseAvailable = false
    },

    hide_notFound() {
      window.setInterval(() => {
        this.notFound = false;
      }, 5000);
    },

    hide_error() {
      window.setInterval(() => {
        this.error = false;
      }, 5000);
    },
  },
  watch: {
    notFound() {
      this.hide_notFound();
    },
    error() {
      this.hide_error();
    },
  }
};
</script>
