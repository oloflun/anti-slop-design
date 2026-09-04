// React Theme — extracted from https://www.whatmattersagency.com
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '24': string;
    '30': string;
    '40': string;
    '98': string;
    '135.434': string;
    '97.7152': string;
    '71.4336': string;
    '57.2768': string;
    '23.1488': string;
    '20.5728': string;
    '19.7152': string;
    '17.7152': string;
 *   };
 *   space: {
    '2': string;
    '12': string;
    '14': string;
    '24': string;
    '27': string;
    '31': string;
    '35': string;
    '39': string;
    '63': string;
    '67': string;
    '70': string;
    '72': string;
    '75': string;
    '93': string;
    '122': string;
    '180': string;
 *   };
 *   radii: {
    xs: string;
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
    "primary": "#fef073",
    "secondary": "#ffa23c",
    "accent": "#5a92e7",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#050505",
    "neutral100": "#ffffff",
    "neutral200": "#6c6b6a",
    "neutral300": "#312821",
    "neutral400": "#f7f7f1"
  },
  "fonts": {
    "body": "'Denim Ink', sans-serif"
  },
  "fontSizes": {
    "24": "24px",
    "30": "30px",
    "40": "40px",
    "98": "98px",
    "135.434": "135.434px",
    "97.7152": "97.7152px",
    "71.4336": "71.4336px",
    "57.2768": "57.2768px",
    "23.1488": "23.1488px",
    "20.5728": "20.5728px",
    "19.7152": "19.7152px",
    "17.7152": "17.7152px"
  },
  "space": {
    "2": "2px",
    "12": "12px",
    "14": "14px",
    "24": "24px",
    "27": "27px",
    "31": "31px",
    "35": "35px",
    "39": "39px",
    "63": "63px",
    "67": "67px",
    "70": "70px",
    "72": "72px",
    "75": "75px",
    "93": "93px",
    "122": "122px",
    "180": "180px"
  },
  "radii": {
    "xs": "2px",
    "full": "800px"
  },
  "shadows": {
    "sm": "rgb(5, 5, 5) 0px 3.6808px 0px 0px"
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
      "main": "#fef073",
      "light": "hsl(54, 99%, 87%)",
      "dark": "hsl(54, 99%, 57%)"
    },
    "secondary": {
      "main": "#ffa23c",
      "light": "hsl(31, 100%, 77%)",
      "dark": "hsl(31, 100%, 47%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#fef073"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#050505"
    }
  },
  "typography": {
    "fontFamily": "'Inter', sans-serif",
    "h1": {
      "fontSize": "40px",
      "fontWeight": "500",
      "lineHeight": "42px"
    }
  },
  "shape": {
    "borderRadius": 2
  },
  "shadows": [
    "rgb(5, 5, 5) 0px 3.6808px 0px 0px"
  ]
};

export default theme;
