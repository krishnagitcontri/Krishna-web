const vscode = require('vscode');

module.exports = class CodeLensProvider {
  _onDidChangeCodeLenses = new vscode.EventEmitter();
  onDidChangeCodeLenses = this._onDidChangeCodeLenses.event;
  async provideCodeLenses(document, token) {
    const codeLenses = [];

    codeLenses.push(
      new vscode.CodeLens(range, {
        title: '',
        tooltip: 'Blackbox Inline',
        command: 'blackbox.comment.chat',
        arguments: [{ name: 'blackbox.comment.chat', selection }],
      })
    );
    return codeLenses;
  }

  fire() {
    this._onDidChangeCodeLenses.fire();
  }
};