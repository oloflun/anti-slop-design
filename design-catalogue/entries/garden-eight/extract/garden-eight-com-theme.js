// React Theme — extracted from https://garden-eight.com/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '0': string;
    '191.104': string;
    '14.85': string;
    '13.05': string;
    '11.7': string;
 *   };
 *   space: {
    '1': string;
    '23': string;
    '40': string;
    '46': string;
    '53': string;
    '76': string;
    '140': string;
    '160': string;
    '185': string;
    '248': string;
 *   };
 *   radii: {
    full: string;
 *   };
 *   shadows: {
    sm: string;
 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "background": "#1e1f1f",
    "foreground": "#dbd6d0",
    "neutral50": "#dbd6d0",
    "neutral100": "#1e1f1f"
  },
  "fonts": {
    "body": "'gunsan', sans-serif"
  },
  "fontSizes": {
    "0": "0px",
    "191.104": "191.104px",
    "14.85": "14.85px",
    "13.05": "13.05px",
    "11.7": "11.7px"
  },
  "space": {
    "1": "1px",
    "23": "23px",
    "40": "40px",
    "46": "46px",
    "53": "53px",
    "76": "76px",
    "140": "140px",
    "160": "160px",
    "185": "185px",
    "248": "248px"
  },
  "radii": {
    "full": "1280px"
  },
  "shadows": {
    "sm": "rgb(30, 31, 31) 0px 2px 2px 0px inset, rgb(219, 214, 208) 0px 3px 2px 0px inset, rgb(219, 214, 208) 0px 3px 3px 0px inset"
  },
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "background": {
      "default": "#1e1f1f",
      "paper": "#1e1f1f"
    },
    "text": {
      "primary": "#dbd6d0",
      "secondary": "#1e1f1f"
    }
  },
  "typography": {
    "fontFamily": "'gunsan', sans-serif",
    "h1": {
      "fontSize": "191.104px",
      "fontWeight": "300",
      "lineHeight": "271.368px"
    },
    "body2": {
      "fontSize": "0px",
      "fontWeight": "600",
      "lineHeight": "0px"
    }
  },
  "shape": {
    "borderRadius": 56
  },
  "shadows": [
    "rgb(30, 31, 31) 0px 2px 2px 0px inset, rgb(219, 214, 208) 0px 3px 2px 0px inset, rgb(219, 214, 208) 0px 3px 3px 0px inset"
  ]
};

export default theme;
