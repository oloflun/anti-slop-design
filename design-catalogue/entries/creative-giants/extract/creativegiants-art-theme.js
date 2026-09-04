// React Theme — extracted from https://creativegiants.art
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
    neutral700: string;
    neutral800: string;
    neutral900: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '80.2584': string;
    '61.1492': string;
    '51.5947': string;
    '32.4855': string;
    '19.1091': string;
    '17.1982': string;
    '15.2873': string;
    '13.3764': string;
    '11.4655': string;
 *   };
 *   space: {
    '1': string;
    '31': string;
    '38': string;
    '46': string;
    '61': string;
    '76': string;
    '107': string;
    '117': string;
    '153': string;
    '173': string;
    '190': string;
    '232': string;
    '255': string;
    '313': string;
    '387': string;
    '400': string;
 *   };
 *   radii: {
    xl: string;
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
    "primary": "#fffef7",
    "secondary": "#009fff",
    "accent": "#ffd001",
    "background": "#fffef7",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#efeeec",
    "neutral200": "#666666",
    "neutral300": "#aaaaaa",
    "neutral400": "#1f1f1f",
    "neutral500": "#131313",
    "neutral600": "#444444",
    "neutral700": "#cccccc",
    "neutral800": "#dddddd",
    "neutral900": "#ecfdf3"
  },
  "fonts": {
    "body": "'Switzer', sans-serif"
  },
  "fontSizes": {
    "80.2584": "80.2584px",
    "61.1492": "61.1492px",
    "51.5947": "51.5947px",
    "32.4855": "32.4855px",
    "19.1091": "19.1091px",
    "17.1982": "17.1982px",
    "15.2873": "15.2873px",
    "13.3764": "13.3764px",
    "11.4655": "11.4655px"
  },
  "space": {
    "1": "1px",
    "31": "31px",
    "38": "38px",
    "46": "46px",
    "61": "61px",
    "76": "76px",
    "107": "107px",
    "117": "117px",
    "153": "153px",
    "173": "173px",
    "190": "190px",
    "232": "232px",
    "255": "255px",
    "313": "313px",
    "387": "387px",
    "400": "400px"
  },
  "radii": {
    "xl": "23px",
    "full": "1529px"
  },
  "shadows": {
    "sm": "rgba(255, 255, 255, 0.2) 0px 0px 0px 1px"
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
    "primary": {
      "main": "#fffef7",
      "light": "hsl(53, 100%, 95%)",
      "dark": "hsl(53, 100%, 83%)"
    },
    "secondary": {
      "main": "#009fff",
      "light": "hsl(203, 100%, 65%)",
      "dark": "hsl(203, 100%, 35%)"
    },
    "background": {
      "default": "#fffef7",
      "paper": "#ffffff"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "32.4855px",
      "fontWeight": "300",
      "lineHeight": "32.4855px"
    },
    "body1": {
      "fontSize": "17.1982px",
      "fontWeight": "300",
      "lineHeight": "17.1982px"
    }
  },
  "shape": {
    "borderRadius": 23
  },
  "shadows": [
    "rgba(255, 255, 255, 0.2) 0px 0px 0px 1px"
  ]
};

export default theme;
