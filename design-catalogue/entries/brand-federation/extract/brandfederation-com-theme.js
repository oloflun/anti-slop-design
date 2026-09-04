// React Theme — extracted from https://www.brandfederation.com/
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '16': string;
    '67.0476': string;
    '36.5714': string;
    '30.4762': string;
    '24.381': string;
    '21.3333': string;
    '15.4286': string;
    '13.7143': string;
    '12.1905': string;
    '9.14286': string;
    '8.22857': string;
 *   };
 *   space: {
    '1': string;
    '6': string;
    '24': string;
    '37': string;
    '48': string;
    '53': string;
    '61': string;
    '69': string;
    '79': string;
    '85': string;
    '98': string;
    '104': string;
    '107': string;
    '128': string;
    '158': string;
    '192': string;
 *   };
 *   radii: {
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {

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
    "primary": "#f56b20",
    "secondary": "#12273e",
    "accent": "#083a74",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#333333",
    "neutral100": "#ffffff",
    "neutral200": "#000000",
    "neutral300": "#edecee",
    "neutral400": "#222222",
    "neutral500": "#a397af",
    "neutral600": "#717d8b",
    "neutral700": "#dddddd"
  },
  "fonts": {
    "body": "'webflow-icons', sans-serif"
  },
  "fontSizes": {
    "16": "16px",
    "67.0476": "67.0476px",
    "36.5714": "36.5714px",
    "30.4762": "30.4762px",
    "24.381": "24.381px",
    "21.3333": "21.3333px",
    "15.4286": "15.4286px",
    "13.7143": "13.7143px",
    "12.1905": "12.1905px",
    "9.14286": "9.14286px",
    "8.22857": "8.22857px"
  },
  "space": {
    "1": "1px",
    "6": "6px",
    "24": "24px",
    "37": "37px",
    "48": "48px",
    "53": "53px",
    "61": "61px",
    "69": "69px",
    "79": "79px",
    "85": "85px",
    "98": "98px",
    "104": "104px",
    "107": "107px",
    "128": "128px",
    "158": "158px",
    "192": "192px"
  },
  "radii": {
    "lg": "12px",
    "xl": "20px",
    "full": "2000px"
  },
  "shadows": {},
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
      "main": "#f56b20",
      "light": "hsl(21, 91%, 69%)",
      "dark": "hsl(21, 91%, 39%)"
    },
    "secondary": {
      "main": "#12273e",
      "light": "hsl(211, 55%, 31%)",
      "dark": "hsl(211, 55%, 10%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#edecee"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#333333"
    }
  },
  "typography": {
    "fontFamily": "'Arial', sans-serif",
    "h1": {
      "fontSize": "36.5714px",
      "fontWeight": "400",
      "lineHeight": "43.8857px"
    },
    "h2": {
      "fontSize": "24.381px",
      "fontWeight": "400",
      "lineHeight": "34.1333px"
    },
    "h3": {
      "fontSize": "21.3333px",
      "fontWeight": "400",
      "lineHeight": "27.7333px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "normal"
    }
  },
  "shape": {
    "borderRadius": 12
  },
  "shadows": []
};

export default theme;
