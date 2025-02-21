name: Second Action
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        id: checkout
        uses: actions/checkout@v3
        with:
          token: ${{ secrets.GLCP_GH_TOKEN }}
          repository: github-action-2025
      - name: Install requirements
        run: pip3 install -r requirements.txt
      - name: Run script
        run: python3 second-action.py
